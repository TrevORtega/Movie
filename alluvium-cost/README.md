# Alluvium: what a daily run costs

Scoping whether `alluvium.py` can run at least once a day, and what it would cost. Status: **first estimate. No live API calls have been made yet.**

## Files

- `alluvium.py`: the script as received, unchanged.
- `estimate_cost.py`: runs the script's own `--dry` rehearsal over N simulated days, with an oracle that records every model call it *would* have made. Prints call counts and token estimates by role, a hard ceiling per day, and $/day by model. Makes no network calls and spends nothing.

```
python estimate_cost.py --days 30                       # script defaults: --cycles 4 --labor 32
python estimate_cost.py --days 5 --cycles 12 --labor 64 # a heavier daily run
```

## How the script spends money

Every model call is one stateless chat-completions request: a system charge plus one user message, about 400–600 input tokens. The script has no conversations, tool loops or growing context, which makes the cost easy to bound.

| Role | When it runs | Calls | Input tok | Output tok (est.) |
|---|---|---|---|---|
| dowser | 2 per *thin* tributary per tide | 1 | ~580 | ~450 |
| scribe | each candidate a dowser returns (≤3) | ≤3 per dowse | ~460 | ~300 |
| assayer | each proposal needs n=3 seals | 1 per seal | ~500 | ~70 |
| winnower | each settled crossing, once | 1 | ~480 | ~250 |
| surveyor | once a month, at freeze | 1 | ~390 | ~150 |
| mill | pure computation | 0 | – | – |

`dig()` makes HTTP HEAD requests to check cited URLs. Those requests are free.

**Hard ceiling.** The scheduler caps each tide at `--labor` tasks (32 by default). Dowsing is the only task that fans out (1 + 3 calls), and at most 10 dowse tasks are possible (5 tributaries × 2). So:

- defaults (`--cycles 4 --labor 32`): **≤ 62 calls/tide, ≤ 248 calls/day, about 124k input + 60k output tokens/day**
- `--cycles 12 --labor 64`: ≤ 1,128 calls/day, about 560k input + 207k output tokens/day

## Cost per day (default settings)

| Model | Ceiling $/day | Ceiling $/month |
|---|---|---|
| Claude Haiku 5.5 ($0.10 / $0.50 per MTok) | $0.04 | ~$1.30 |
| Claude Haiku 4.5 ($1 / $5) | $0.42 | ~$13 |
| Claude Sonnet 5.5 ($2 / $10) | $0.85 | ~$25 |
| Claude Opus 5.5 ($4 / $20) | $1.70 | ~$51 |
| Self-hosted (Ollama, llama.cpp, vLLM) | $0 (your hardware) | – |

These are worst cases. Every day is assumed to hit the ceiling, and hidden reasoning tokens are not counted (see caveats). In the 30-day simulation, day 1 reached 243 of the 248 possible calls. Day 2 made 194 and day 3 made 134.

**Why it won't stay at the ceiling.** The scheduler sends dowsers only to tributaries still below their `floor` (12/10/10/8/12 settled states, 52 in total). Once every floor is met, dowsing stops. After that the only work is sealing and winnowing whatever is still pending, and a daily run then costs close to nothing. If the register is meant to keep growing, the floors have to be raised, and the real cost is set by those floors rather than by how often it runs. (The dry run levels off at 32 calls/day only because the rehearsal's fake source bank runs out of new names. A live run behaves differently.)

**Bottom line:** at default settings on a cheap model, the API bill is cents per day. The compute that hosts the daily job probably costs more than the API.

## Caveats and things to verify before a live run

1. **Thinking tokens.** Current Claude models have adaptive thinking on by default, and thinking is billed as output. Thinking cannot be disabled on Opus 5.5. On Haiku 5.5 it can be turned off only at effort `high` or below. The script never sets this, so the output column could be 2–5× higher. Measure it with one live run.
2. **API compatibility.** The script speaks the OpenAI-style `/chat/completions` dialect and sends `temperature` on every call. It sets no `max_tokens`. The Anthropic Messages API (version 2026-10-21) rejects `temperature`. Before choosing Claude, check whether Anthropic's OpenAI-compatible endpoint accepts these requests as written. If it doesn't, the `Oracle` class needs a small adapter. OpenRouter or a local server would take the requests unchanged.
3. **Output sizes are estimates.** They come from each role's JSON shape, not from measurement. Token counts use about 4 characters per token.
4. **Model mix.** Ordinance 3 recommends several models (`ALLUVIUM_MODELS=a,b,c`). Each laborer is hashed to one model, so the cost is roughly the average of the chosen models' prices.

## Hosting the daily run

- **Runtime:** ≤248 calls with 8 workers at a few seconds each, so about 2–5 minutes a day.
- **State:** the register (`./alluvium/strata.jsonl` and `almanac/`) has to survive between runs. Runs are cumulative ("the bed remembers").
- **Options:**
  - **GitHub Actions cron:** free within the minutes allowance. The job must persist the register, either by committing it back or by using artifacts or a cache. The API key goes in repo secrets.
  - **Small VM or always-on box with cron:** about $4–6/month. This is the simplest way to keep state.
  - **Self-hosted model on your own machine:** $0 API cost. Slower, and only as good as the local model.

## Live runs (`live_run.py`)

`alluvium.py` can't be pointed at Claude unchanged. Anthropic's OpenAI-compatible endpoint (`https://api.anthropic.com/v1`) returns **400 for any `temperature` below 1** on Claude 4.7 and later models, and the script sends 0.2–0.9 on every call. It also doesn't retry a 400, so every laborer "falls" and the run ends with an empty register. A test against a local mock with the same rule confirmed this: all 8 of 8 tasks failed.

`live_run.py` runs the same register and tides without editing `alluvium.py`. Its oracle:
- omits `temperature`;
- sets `max_tokens` (8000 by default);
- logs each response's real `usage` to `<root>/usage.jsonl`;
- stops making calls once `--budget-usd` is spent;
- makes one preflight call first, so a bad key or model name fails immediately.

It reads the key from **`ALLUVIUM_API_KEY`**. The completion tokens it records include hidden thinking, which is what you're billed for.

```
# 1. Haiku smoke test: 1 tide of 8 tasks, about 30-40 calls, a few cents at most
python live_run.py --model claude-haiku-5-5 --cycles 1 --labor 8 --budget-usd 0.25

# 2. Sonnet real run: script defaults (4 tides x 32 tasks, <=248 calls), fresh register
python live_run.py --model claude-sonnet-5-5 --budget-usd 5
```

Each model gets its own register under `runs/<model>/`, so the smoke test never mixes into the real run. Both commands print usage by role, any failed calls, the register tally, and a projected cost for a full default day.

## Next steps

1. Add `ALLUVIUM_API_KEY` to the environment, then run the Haiku smoke test above.
2. Put those measured numbers into `OUTPUT_TOKENS` / `PRICES` in `estimate_cost.py` and re-estimate.
3. Decide how to persist state, then wire up the daily schedule.
