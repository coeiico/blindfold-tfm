# blindfold-tfm

**Board-game world model.** Does a transformer trained only on move sequences build an internal picture of the board it never sees?

**Status:** not started.

## Question

Does a model trained only on move sequences build an internal picture of the board it never sees?

## Plan

- **Architecture:** tiny-transformer, 6–8 layers.
- **Data:** synthetic games of random legal moves. Warm up on tic-tac-toe, then Connect Four (its engine is reused by four-from-zero-resnet) or 6×6 Othello.

## Experiments

- Legal-move rate on held-out games.
- Linear probes for each square (empty, mine, theirs, relative to the player to move, which made probes linear in Othello-GPT follow-up work).
- A randomly initialized control.
- Interventions that flip a square in the representation and check that predicted legal moves change to match.

## Done when

- Probes clearly beat the control, and at least one intervention changes legal-move predictions as expected.

Plus the general checklist:

Apply this checklist with the project-specific requirements and exceptions in
[CLAUDE.md](CLAUDE.md#project-specific-scope).

- `just quick` runs end to end on CPU in under 5 minutes, as a smoke test.
- The full run fits on one consumer GPU (8–12 GB VRAM) and auto-detects cuda, mps or cpu.
- Each run saves weights, `metrics.json` and its plots to `runs/<run-name>/`.
- This README shows the headline result with plots, compares against baselines, and states negative results plainly.
- Tests cover data generators, tensor shapes and one tiny overfit check.

## Notes

- The Connect Four engine written here is reused by four-from-zero-resnet, and the probe and intervention code is reused by tiny-trace-tfm, so keep both clean and importable.

## Quickstart

Needs [uv](https://docs.astral.sh/uv/) and [just](https://just.systems/). Everything else, Python 3.12 included, comes from uv.

```sh
just setup              # uv sync, then install the pre-commit hooks
just quick              # CPU smoke test, under 5 minutes
just train              # full run; flags pass through, e.g. --run-name wd1.0-seed0
just analyze <run>      # baselines, probes, interventions and plots
just cloud <sweep>      # the same runs on Modal, one GPU each; see .agents/instructions/cloud.md
just test               # pytest
just check              # ruff and basedpyright, as in CI
```

Copy `.env.example` to `.env` (gitignored) for `HF_TOKEN` and `HF_USER`.

This repo builds on [tiny-transformer](https://github.com/coeiico/tiny-transformer), installed from GitHub. To work on both at once, run `uv add --editable ../tiny-transformer`, then switch back to the git source before committing.

## Layout

```
blindfold-tfm/
├── README.md                goal, plan, results with plots
├── CLAUDE.md                instructions for coding agents; AGENTS.md points here
├── .agents/                 instructions/ (Python formatting, commits) and plans/
├── pyproject.toml           metadata, dependencies, tool settings
├── uv.lock                  committed lockfile
├── .python-version          pinned by uv
├── justfile                 every routine command
├── .pre-commit-config.yaml
├── .github/workflows/ci.yml
├── src/blindfold_tfm/
│   └── model.py, data.py, analysis.py, utils.py
├── train.py                 CLI; --quick runs the CPU smoke test
├── predict.py               load weights and run inference
├── analyze.py               baselines, probes, interventions, plots
├── cloud.py                 the same runs on Modal, one GPU per run
├── figures/                 README figures: LaTeX sources, data and built PNGs
├── notebooks/               marimo notebooks for exploration
├── tests/
└── runs/                    outputs, gitignored
```

## Results

_No results yet._ The headline result with plots, the comparison against baselines, and any negative results go here.

## Sources

- Li et al. 2023, Emergent world representations (Othello-GPT)
- Nanda et al. 2023, Emergent linear representations

## License

MIT
