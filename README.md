# re-journey

A research engineer's lab notebook. Small experiments on neural nets, LLMs and evaluations, written up honestly: what I tried, what the numbers said, and what I still don't understand.

Built in public over 90 days (16 Nov 2026 to 14 Feb 2027).

## How this repo works

| Folder | What goes there |
|---|---|
| `weeks/` | One folder per week: the goals and the code I wrote to meet them |
| `labnotes/` | Short notes after each session, from `labnotes/TEMPLATE.md` |
| `experiments/` | Real experiments. Each starts with a written plan before any code |
| `skills/` | Instructions any AI assistant can follow (Claude Code, Codex, GPT): plan an experiment, write a lab note, check a plot, review the week |
| `src/rej/` | Small shared helpers (seeding, plotting) |

## The 90 days

| Weeks | Phase | Main output |
|---|---|---|
| 1–4 | Foundations | micrograd, makemore, MNIST MLP |
| 5 | Buffer | catch up or rest |
| 6–9 | Transformers + evaluations | tiny GPT, evaluation statistics, LLM-as-a-judge reading, experiment plan |
| 10 | Buffer | |
| 11–13 | First experiment | Can an LLM grade like a teacher? Baseline, ablations, write-up, video |

## Rules I follow

- 25 minutes a day counts as a full day.
- Hypothesis and metric are written before code.
- Every result is compared to a baseline.
- Numbers are reported as they came out, including the bad ones.

## Run

```bash
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
pytest -q
```

## License

MIT
