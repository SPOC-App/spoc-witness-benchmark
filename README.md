# SPOC witness benchmark: scenarios, prompts, votes and scripts

This folder holds the material behind the method note in METHOD_NOTE.md: a test of whether language models can tell when an AI agent's steps depart from the purpose it was given. Read the note first, including its limits. The test uses scripted, synthetic traces. It says nothing about live agents and is not independent validation.

## Contents
- METHOD_NOTE.md: method, results, errors, disputed labels, limits and claims.
- data/scenarios: the 158 scripted traces with expected labels (round 1 development and hold-out, round 2, round 3).
- data/votes: every model verdict and rationale, one line per trace, model and repeat. Rationales are AI-generated outputs from the models named in the note, obtained through the Perplexity platform. Each file name says which prompt version was used.
- data/manifests: the hashes recorded before each round was run.
- prompts: the exact reviewer prompts, v1 and v2.
- docs: the reviewer rubrics with design reasons, the benchmark plan and the per-round results records.
- scripts/analyse.py: recomputes every detection and false-positive figure from the saved votes.
- scripts/run_review.py: the runner outline. Connect call_model() to a model provider to rerun.

## Check the figures
    python scripts/analyse.py data/votes/round3-v2.jsonl data/scenarios/round3.json
    python scripts/analyse.py data/votes/round2-v1.jsonl data/scenarios/round2.json
    python scripts/analyse.py data/votes/round1-v1.jsonl data/scenarios/round1-development.json data/scenarios/round1-holdout.json

## Naming and claims
Model names identify what was tested and imply no endorsement by or affiliation with the providers. Findings describe deviation from a declared scope or purpose, never bad faith.

## Licence
Data, prompts, documents and the method note: Creative Commons Attribution 4.0 International (LICENSE-DATA-AND-DOCS.txt). Scripts in the scripts folder: MIT (LICENSE-SCRIPTS.txt).

## Scope of this release
The rule-based checks and the replay tool described in the note are not part of this release.
