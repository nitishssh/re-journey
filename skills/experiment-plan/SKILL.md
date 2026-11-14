---
name: experiment-plan
description: Turn a research question into a written experiment plan before any code is run. Use when asked to "plan an experiment", "design a study", or before starting a new folder in experiments/.
---

# Experiment plan

1. Ask for the question in one sentence. Refuse to start coding until it exists.
2. Copy `experiments/TEMPLATE.md` to `experiments/<yyyy-mm-dd>-<slug>/PLAN.md`.
3. Fill every section. Force these choices explicitly:
   - a **baseline** (simplest thing that could work, or chance level)
   - at least **one ablation**
   - the **metric** with its formula, and how variance is measured (seeds, bootstrap CI)
   - the result that would **prove the hypothesis wrong**
4. Flag data risk: real student or personal data is never used; synthetic or anonymized only.
5. Stop and show the plan. Code comes in a separate step.
