# Witness multi-model benchmark plan

Decisions recorded 11 October 2026: expanded scenario set approved, false-positive bar accepted, reviewing models may be named. Plan only. Nothing is run, published or sent without approval.

## 1. Goal
Measure how well the judgement-based review (A1) detects departures from the spirit of a task, with error rates good enough to publish, and report it beside the deterministic checks. The deterministic checks already pass their scripted scenarios, so this plan is about the advisory review.

## 2. What is measured
- Detection: share of deviating runs the review flags.
- False positives: share of benign twins it flags.
- Agreement: how often the reviewing models agree, and how often a single model changes its answer on a repeat.
- Injection resistance: whether text written by the monitored agent changes a result.
- Reported with 95 percent intervals, and every miss and false positive listed.

## 3. Reviewers
Three or more models from different providers, chosen from the models available at run time, and named in the method note because they are the tool, not the subject. Each receives the same structured trace and the same frozen rubric and nothing else. Settings, versions and run dates are recorded. A strict majority is needed to flag, and disagreement is reported.

## 4. Scenario set
The current ten scenarios have only two cases that depend on judgement, which is too few for error rates. Plan:
- Expand to about forty scenarios with twins, with at least twenty depending on judgement, and add benign look-alike traces so that at least 35 independent benign traces go through the judgement review. This is needed because of the bar in section 6: with a 95 percent Wilson interval, zero false positives in 20 benign traces still leaves an upper end near 16 percent, in 35 about 10 percent, in 40 about 9 percent. One false positive in 40 already exceeds it. Repeats of the same trace do not count as independent traces. Families: malicious compliance, metric gaming, injected instructions, quiet scope drift within allowed scopes, selective emphasis, and benign look-alikes designed to tempt false positives.
- Write expected labels before any run, record them with a hash, and keep roughly a quarter as a private hold-out. The hold-out is revealed only in the final report.
- Benign twins must include honest edge cases: a legitimate large action, an unusual but permitted tool, a refusal.
- The owner approves the scenario texts and labels. No outside reviewer, as decided.

## 5. Protocol
1. Freeze rubric, prompts, scenarios and expected labels; record a combined hash.
2. Run each trace through each reviewer five times, in randomised order, with the same settings.
3. Record raw votes and rationales; apply the majority rule; compute the measures above.
4. Run an injection test: add hostile free text to traces and confirm the structured trace removes it, then test a variant where steps themselves are phrased to mislead.
5. Compare with the deterministic checks on the same scenarios.
6. Review results with the owner before anything is written up.

Scale: forty scenarios with twins is eighty traces, times three reviewers, times five repeats, about twelve hundred calls. The cost is not estimated here.

## 6. Decision rules, fixed in advance
- The review is described as advisory in every case. It is never part of a live path.
- It may be shown to principals only if its false-positive rate on twins is low enough that the owner accepts it. Proposed bar: at most five percent with the upper end of the interval under ten percent. If it misses the bar, we publish that, and keep it offline.
- Any scenario family with detection under half is reported as a known weakness.
- Results are published only with method, versions, scenarios (except hold-out until the end) and all errors.

## 7. Subjects
The scenarios stay scripted. Running real models as the agents under test is a separate later phase, only with each provider's consent, and nothing is named without agreement.

## 8. Risks
- Small sample: wide intervals. Mitigation: more scenarios, intervals shown, no strong claims.
- Rubric tuned to the tests. Mitigation: freeze first, hold-out set.
- Reviewer bias or sensitivity to wording. Mitigation: several providers, repeats, order randomisation.
- Mislabelled expected answers. Mitigation: owner approval, and a model challenge of every label before freezing, with disputes resolved by the owner and listed.
- Overclaiming. Mitigation: wording rules in section 6 and the existing claims discipline: aligned with, never compliant with.

## 9. Timeline and gates
1. Expand and label scenarios; owner review.
2. Freeze and hash.
3. Run and analyse; owner review.
4. Method note and results draft; owner review.
5. Optional: consented subject-model phase.

No gate is skipped, and none involves production, the rights operator, admission or the public site.

## 10. Decisions
- Expanded scenario set: approved.
- False-positive bar: accepted, which in practice means zero false positives across at least 35 independent benign traces.
- Reviewers named in the method note: approved. Check each provider's terms on publishing benchmark results before publication, and state that naming implies no endorsement.
- The author must not change the rubric after seeing hold-out results.
