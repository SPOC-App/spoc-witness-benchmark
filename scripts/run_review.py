"""Send each scenario to a reviewing model five times and save the verdicts.

Usage: python run_review.py <scenarios.json> <prompt.txt> <model-name> <out.jsonl> [seed]

call_model() is a placeholder: connect it to any model provider that can return
{"flag": bool, "rationale": str}. The original runs used one trace per call,
five repeats per trace, a fixed shuffled order and service default settings.
"""
import json, random, sys

def trace(s):
    steps = [{k: v for k, v in e.items() if v is not None} for e in s["steps"]]
    return json.dumps({"purpose": s["purpose"], "scopes": s["scopes"],
                       "preconditions": s.get("preconditions", []), "steps": steps})

def call_model(model, prompt, trace_json):
    raise NotImplementedError("connect your model provider here")

def main():
    scen, prompt_file, model, out = sys.argv[1:5]
    seed = int(sys.argv[5]) if len(sys.argv) > 5 else 1
    prompt = open(prompt_file).read()
    sc = json.load(open(scen))["scenarios"]
    jobs = [(s, r) for s in sc for r in range(5)]
    random.Random(seed).shuffle(jobs)
    with open(out, "a") as f:
        for s, r in jobs:
            res = call_model(model, prompt, trace(s))
            f.write(json.dumps({"model": model, "id": s["id"], "rep": r, "result": res}) + "\n")

if __name__ == "__main__":
    main()
