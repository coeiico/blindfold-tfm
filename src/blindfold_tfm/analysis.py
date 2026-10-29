"""
Baselines, probes and interventions, run on saved weights.

Experiments:
- Legal-move rate on held-out games.
- Linear probes for each square (empty, mine, theirs, relative to the player to move,
  which made probes linear in Othello-GPT follow-up work).
- A randomly initialized control.
- Interventions that flip a square in the representation and check that predicted legal
  moves change to match.
"""

# TODO: implement. See README.md for the plan.
