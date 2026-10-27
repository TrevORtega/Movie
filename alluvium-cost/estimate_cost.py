#!/usr/bin/env python3
"""Estimate what running alluvium.py once a day would cost.

Runs the script's own --dry rehearsal (no network, no API spend) for a number
of simulated days, with an oracle that records every model call it would have
made: which role, and how large the prompt was. Prompt sizes are measured from
the real charges; output sizes cannot be measured offline, so they come from
the per-role estimates in OUTPUT_TOKENS below. Tokens are estimated at
CHARS_PER_TOKEN characters each.

    python estimate_cost.py                       # 30 days, defaults
    python estimate_cost.py --days 30 --cycles 4 --labor 32
"""
from __future__ import annotations

import argparse
import contextlib
import io
import re
import sys
import tempfile
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import alluvium  # noqa: E402

CHARS_PER_TOKEN = 4.0

# Visible output tokens per call, by role, read off each role's JSON shape.
# Dowser: 3 candidates x ~5 fields. Scribe: 4-7 destructor phrases.
# Winnower: one attack, 6 fields. Assayer: verdict + one sentence.
OUTPUT_TOKENS = {"dowser": 450, "scribe": 300, "winnower": 250, "assayer": 70, "surveyor": 150}

# USD per million tokens (input, output). Edit to match your provider.
PRICES = {
    "Claude Haiku 5.5":   (0.10, 0.50),
    "Claude Haiku 4.5":   (1.00, 5.00),
    "Claude Sonnet 5.5":  (2.00, 10.00),
    "Claude Opus 5.5":    (4.00, 20.00),
    "self-hosted (Ollama etc.)": (0.0, 0.0),
}


class CountingSpring(alluvium.DrySpring):
    def __init__(self) -> None:
        super().__init__()
        self.calls: list[tuple[str, int]] = []  # (role, input chars)

    def ask(self, system: str, user: str, *, agent: str, temperature: float = 0.7) -> str:
        role = re.search(r"\[ROLE: (\w+)\]", system).group(1)
        self.calls.append((role, len(system) + len(user)))
        return super().ask(system, user, agent=agent, temperature=temperature)


def simulate(days: int, cycles: int, labor: int, workers: int) -> list[list[tuple[str, int]]]:
    """One list of calls per simulated day, against a register that persists across days."""
    per_day = []
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp) / "register"
        for _ in range(days):
            oracle = CountingSpring()
            with contextlib.redirect_stderr(io.StringIO()):
                sediment = alluvium.Sediment(root, rehearsal=True)
                alluvium.seed(sediment)
                alluvium.Watershed(oracle, sediment, alluvium.Ordinances(labor=labor), workers).run(cycles, freeze=False)
            per_day.append(oracle.calls)
    return per_day


def tokens(calls: list[tuple[str, int]]) -> tuple[float, float]:
    tin = sum(c for _, c in calls) / CHARS_PER_TOKEN
    tout = sum(OUTPUT_TOKENS[r] for r, _ in calls)
    return tin, tout


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--days", type=int, default=30)
    ap.add_argument("--cycles", type=int, default=4, help="tides per daily run (script default 4)")
    ap.add_argument("--labor", type=int, default=32, help="tasks per tide (script default 32)")
    ap.add_argument("--workers", type=int, default=8)
    args = ap.parse_args()

    per_day = simulate(args.days, args.cycles, args.labor, args.workers)

    print(f"Simulated {args.days} daily runs of --cycles {args.cycles} --labor {args.labor}\n")
    print("day  calls  dowse scribe winnow assay survey   in_tok  out_tok")
    for i, calls in enumerate(per_day, 1):
        n = defaultdict(int)
        for r, _ in calls:
            n[r] += 1
        tin, tout = tokens(calls)
        print(f"{i:>3} {len(calls):>6} {n['dowser']:>6} {n['scribe']:>6} {n['winnower']:>6} "
              f"{n['assayer']:>5} {n['surveyor']:>6} {tin:>8.0f} {tout:>8.0f}")

    flat = [c for day in per_day for c in day]
    by_role = defaultdict(list)
    for r, c in flat:
        by_role[r].append(c)
    print("\nAverage prompt size by role (tokens):")
    for r, cs in sorted(by_role.items()):
        print(f"  {r:<9} {sum(cs) / len(cs) / CHARS_PER_TOKEN:>6.0f} in  ~{OUTPUT_TOKENS[r]} out  ({len(cs)} calls)")

    # Hard ceiling from the scheduler: each thin tributary gets 2 dowse tasks,
    # each dowse is 1 dowser call + up to 3 scribe calls; every other task is 1 call.
    ords = alluvium.Ordinances(labor=args.labor)
    thin_max = sum(1 for t in alluvium.TRIBUTARIES if t.name != "the mill")
    dowse_tasks = min(args.labor, thin_max * ords.dowsers_per_thin)
    per_tide = dowse_tasks * (1 + ords.candidates_per_dowser) + (args.labor - dowse_tasks)
    avg_tok = {r: sum(cs) / len(cs) / CHARS_PER_TOKEN for r, cs in by_role.items()}
    tide_in = (dowse_tasks * (avg_tok["dowser"] + ords.candidates_per_dowser * avg_tok["scribe"])
               + (args.labor - dowse_tasks) * avg_tok["assayer"])
    tide_out = (dowse_tasks * (OUTPUT_TOKENS["dowser"] + ords.candidates_per_dowser * OUTPUT_TOKENS["scribe"])
                + (args.labor - dowse_tasks) * OUTPUT_TOKENS["assayer"])
    print(f"\nCeiling: {per_tide} calls/tide, {per_tide * args.cycles} calls/day, "
          f"~{tide_in * args.cycles:,.0f} in / {tide_out * args.cycles:,.0f} out tokens/day")
    for model, (pin, pout) in PRICES.items():
        print(f"  {model:<28} ${(tide_in * pin + tide_out * pout) * args.cycles / 1e6:.3f}/day max")

    worst = max(per_day, key=lambda d: sum(tokens(d)))
    avg_in = sum(tokens(d)[0] for d in per_day) / len(per_day)
    avg_out = sum(tokens(d)[1] for d in per_day) / len(per_day)
    w_in, w_out = tokens(worst)
    print(f"\nPer day: avg {avg_in:,.0f} in / {avg_out:,.0f} out tokens; busiest day {w_in:,.0f} in / {w_out:,.0f} out")
    print(f"\n{'model':<28}{'avg $/day':>10}{'busiest $/day':>15}{'$/month (avg)':>15}")
    for model, (pin, pout) in PRICES.items():
        avg = (avg_in * pin + avg_out * pout) / 1e6
        busy = (w_in * pin + w_out * pout) / 1e6
        print(f"{model:<28}{avg:>10.3f}{busy:>15.3f}{avg * 30:>15.2f}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
