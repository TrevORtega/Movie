#!/usr/bin/env python3
"""Run alluvium.py live against Claude, metering every call.

Uses Anthropic's OpenAI-compatible endpoint, which alluvium's Oracle already
speaks, with three changes made here rather than in alluvium.py:

  - no `temperature`: Claude 4.7+ models (Haiku 5.5, Sonnet 5.5) reject any
    value below 1 with a 400, and alluvium sends 0.2-0.9 on every call;
  - an explicit `max_tokens`, so a long answer cannot run away;
  - every response's `usage` is logged to <root>/usage.jsonl, and the run
    stops calling once --budget-usd is spent.

Reads the key from ALLUVIUM_API_KEY.

    python live_run.py --model claude-haiku-5-5 --cycles 1 --labor 8 --budget-usd 0.25
    python live_run.py --model claude-sonnet-5-5 --budget-usd 3
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import threading
import time
import urllib.error
import urllib.request
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import alluvium  # noqa: E402

DEFAULT_BASE = "https://api.anthropic.com/v1"

# USD per million tokens (input, output).
PRICES = {
    "claude-haiku-5-5":  (0.10, 0.50),
    "claude-haiku-4-5":  (1.00, 5.00),
    "claude-sonnet-5-5": (2.00, 10.00),
    "claude-opus-5-5":   (4.00, 20.00),
}


class BudgetSpent(RuntimeError):
    pass


class MeteredOracle(alluvium.Oracle):
    def __init__(self, base: str, key: str, model: str, *, max_tokens: int, budget_usd: float,
                 log_path: Path, thinking: dict | None = None):
        super().__init__(base, key, [model])
        self.model = model
        self.max_tokens = max_tokens
        self.budget_usd = budget_usd
        self.thinking = thinking
        self.price_in, self.price_out = PRICES[model]
        self.log_path = log_path
        self.lock = threading.Lock()
        self.spent = 0.0
        self.by_role: dict[str, dict[str, float]] = defaultdict(lambda: defaultdict(float))
        self.errors: list[str] = []

    def _record(self, role: str, usage: dict, seconds: float, finish: str) -> None:
        pin, pout = usage.get("prompt_tokens", 0), usage.get("completion_tokens", 0)
        cost = (pin * self.price_in + pout * self.price_out) / 1e6
        with self.lock:
            self.spent += cost
            r = self.by_role[role]
            r["calls"] += 1
            r["in"] += pin
            r["out"] += pout
            r["usd"] += cost
            r["truncated"] += finish == "length"
            with self.log_path.open("a") as f:
                f.write(json.dumps({"when": alluvium.now(), "role": role, "model": self.model,
                                    "prompt_tokens": pin, "completion_tokens": pout, "usd": round(cost, 6),
                                    "seconds": round(seconds, 2), "finish_reason": finish}) + "\n")

    def ask(self, system: str, user: str, *, agent: str, temperature: float = 0.7) -> str:
        m = re.search(r"\[ROLE: (\w+)\]", system)
        role = m.group(1) if m else "other"
        with self.lock:
            if self.spent >= self.budget_usd:
                raise BudgetSpent(f"budget of ${self.budget_usd:.2f} spent")
        payload = {"model": self.model, "max_tokens": self.max_tokens,
                   "messages": [{"role": "system", "content": system}, {"role": "user", "content": user}]}
        if self.thinking is not None:
            payload["thinking"] = self.thinking
        body = json.dumps(payload).encode("utf-8")
        headers = {"Content-Type": "application/json", "User-Agent": "alluvium/1",
                   "Authorization": f"Bearer {self.key}"}
        delay = 1.0
        for _ in range(self.patience):
            req = urllib.request.Request(self.base + "/chat/completions", data=body, headers=headers, method="POST")
            started = time.monotonic()
            try:
                with urllib.request.urlopen(req, timeout=self.timeout) as r:
                    data = json.loads(r.read().decode("utf-8"))
                choice = data["choices"][0]
                self._record(role, data.get("usage") or {}, time.monotonic() - started,
                             choice.get("finish_reason") or "")
                return choice["message"]["content"] or ""
            except urllib.error.HTTPError as e:
                if e.code in (408, 409, 425, 429) or e.code >= 500:
                    time.sleep(delay)
                    delay = min(delay * 2, 30)
                    continue
                detail = e.read().decode("utf-8", "replace")[:500]
                with self.lock:
                    self.errors.append(f"{role}: HTTP {e.code}: {detail}")
                raise
            except (urllib.error.URLError, TimeoutError, OSError):
                time.sleep(delay)
                delay = min(delay * 2, 30)
        with self.lock:
            self.errors.append(f"{role}: no answer after {self.patience} tries")
        raise RuntimeError("the oracle did not answer after patient asking")


def report(oracle: MeteredOracle, sediment: alluvium.Sediment, cycles: int) -> None:
    print(f"\n== {oracle.model}: {cycles} tide(s), ${oracle.spent:.4f} spent of ${oracle.budget_usd:.2f} budget ==")
    print(f"{'role':<10}{'calls':>6}{'avg in':>8}{'avg out':>9}{'truncated':>11}{'usd':>10}")
    for role, r in sorted(oracle.by_role.items()):
        n = r["calls"]
        print(f"{role:<10}{n:>6.0f}{r['in'] / n:>8.0f}{r['out'] / n:>9.0f}{r['truncated']:>11.0f}{r['usd']:>10.4f}")
    if oracle.errors:
        print(f"\n{len(oracle.errors)} failed call(s); first few:")
        for e in oracle.errors[:5]:
            print("  " + e)
    t = sediment.tally()
    print(f"\nregister: {t['settled']} settled, {t['suspended']} awaiting seals, "
          f"{t['washed']} washed, {t['mirages']} mirages")
    calls = sum(r["calls"] for r in oracle.by_role.values())
    if calls:
        # Project a full default day (the 248-call ceiling) from measured per-call cost by role.
        per_call = {role: r["usd"] / r["calls"] for role, r in oracle.by_role.items()}
        dowse = per_call.get("dowser", 0) + 3 * per_call.get("scribe", 0)
        other = per_call.get("assayer", sum(per_call.values()) / len(per_call))
        ceiling = 4 * (10 * dowse + 22 * other)
        print(f"projected default-day ceiling (4 tides x 32 tasks) on {oracle.model}: ${ceiling:.2f}")
        for model, (pin, pout) in PRICES.items():
            if model != oracle.model:
                scale_in = sum(r["in"] for r in oracle.by_role.values())
                scale_out = sum(r["out"] for r in oracle.by_role.values())
                same_tokens = (scale_in * pin + scale_out * pout) / 1e6
                print(f"  same tokens on {model}: ${same_tokens:.4f} (this run)")


def preflight(oracle: MeteredOracle) -> None:
    """One tiny call, so a bad key, model name or request shape fails before the tides start."""
    oracle.ask("[ROLE: preflight]\nAnswer with JSON only.", 'Reply with {"ok": true}', agent="preflight")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", required=True, choices=sorted(PRICES))
    ap.add_argument("--root", type=Path, default=None, help="register directory (default runs/<model>)")
    ap.add_argument("--cycles", type=int, default=4)
    ap.add_argument("--labor", type=int, default=32)
    ap.add_argument("--workers", type=int, default=8)
    ap.add_argument("--max-tokens", type=int, default=8000)
    ap.add_argument("--budget-usd", type=float, required=True, help="stop calling once this much is spent")
    ap.add_argument("--thinking", default=None,
                    help='JSON passed as the request\'s "thinking" field, e.g. \'{"type": "disabled"}\'; '
                         "default leaves the model's own default (adaptive thinking on Claude 5 models)")
    args = ap.parse_args()

    key = os.environ.get("ALLUVIUM_API_KEY", "").strip()
    if not key:
        print("ALLUVIUM_API_KEY is not set.", file=sys.stderr)
        return 2
    base = os.environ.get("ALLUVIUM_API_BASE", DEFAULT_BASE).strip()
    root = args.root or Path(__file__).resolve().parent / "runs" / args.model
    root.mkdir(parents=True, exist_ok=True)

    oracle = MeteredOracle(base, key, args.model, max_tokens=args.max_tokens, budget_usd=args.budget_usd,
                           log_path=root / "usage.jsonl",
                           thinking=json.loads(args.thinking) if args.thinking else None)
    try:
        preflight(oracle)
    except Exception as e:
        print(f"preflight failed: {e}", *oracle.errors, sep="\n", file=sys.stderr)
        return 1

    sediment = alluvium.Sediment(root, rehearsal=False)
    alluvium.seed(sediment)
    alluvium.Watershed(oracle, sediment, alluvium.Ordinances(labor=args.labor), args.workers).run(args.cycles, freeze=False)
    report(oracle, sediment, args.cycles)
    return 0


if __name__ == "__main__":
    sys.exit(main())
