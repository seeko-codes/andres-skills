# Test the model, the implementation, and the cost

Read when evaluating a substantial structural change, comparing approaches, or designing
an experiment to resolve consequential uncertainty. This supplies acceptance evidence to
the current task; it is not a mandatory suite for every edit or a separate delivery stage.

## Define what could fail before claiming improvement

Keep the agreed outcome and mandatory constraints fixed during a comparison. Select checks
for affected claims and name their pass/fail conditions before observing results. If the
human changes acceptance, record the change and do not compare it as the same task.
Use existing project gates and the current quality policy; do not invent behavioral tests
for documentation-only work or weaken tests to make a candidate look successful.

| Claim | Useful check | Failure evidence |
|---|---|---|
| The solution logic predicts where and how the problem is solved | Before inspecting a held-out case, identify the target responsibility, required support, defensible exclusions, and expected behavior | Missed necessary dependencies, incorrect behavior prediction, or an explanation compatible with every outcome |
| An abstraction earns its place | Challenge its removal or combination: which required distinction, contract, or representative change becomes worse? Use a bounded experiment when judgment alone cannot settle it | Added indirection with no identified benefit, or a boundary that requires callers to reconstruct hidden implementation |
| The implementation fulfills its contract | Existing behavior, boundary, regression, integration, and relevant visual checks selected by the quality owner | An unmet acceptance condition or broken affected contract, regardless of how plausible the design sounds |
| Structure supports change | Exercise a representative bounded change, preserving external contracts and checking affected consumers | Unexpected coupling or broad reconstruction; raw file count alone is not a verdict |
| The process is more economical | Compare matched tasks and quality against the simpler existing approach | Savings disappear when failures, verification, rework, or maintenance are counted; reduced reads miss necessary evidence |

A held-out case was not used to construct or tune the explanation. Use a fresh evaluator
or unexamined case when feasible; label a self-review or simulated walkthrough honestly.
These checks can falsify particular claims of elegance, not prove a globally minimal design.
Treat unresolved necessity as a question, not permission to delete a working abstraction.

## Keep measurements cheap and distinct

- **Peak context:** live occupied context and completion headroom, governed by orchestration
  or local budget policy. Report measured, estimated (with method), or unknown.
- **Total processing/cost:** aggregate relevant model/tool work across workers, retries,
  and handoffs using available usage/cost records. Billing is useful here, not as occupancy.
- **Elapsed time:** end-to-end latency; separate agent work from external/human waiting
  where observable. A faster finish can still consume more aggregate work.
- **Rework and maintenance:** failed attempts, later repairs, and updating durable structure.
  Report an observation window and deferred/unknown costs rather than assuming zero.

An optional routing proxy is:

    Context waste ≈ unnecessary material read / total material read

Include orientation, summaries, and detours; account for material-size differences. Judge
necessity against verified task evidence. Report absolute reading cost alongside the ratio:
a lower fraction can hide greater total waste. Neither measure is live occupancy.

Include all attempts and completion/failure rates, not only cheap successful runs. Use the
same starting artifacts, acceptance, and comparable model/effort/tool conditions; record
confounds. Repeat representative tasks when practical and show variation, not just a best
run. No universal improvement threshold is prescribed. A cost improvement cannot compensate
for failing a required quality gate; non-dominated tradeoffs need explicit judgment.

## One small experiment at a time

Use existing plan or brief fields to record: the consequential question; observations that
would distinguish candidate explanations; the bounded action and stopping evidence; then
the actual result, correction, and next step. This is a conclusion record, not private
reasoning or a logging requirement for every tool call.

For progress lost on reload, inspecting stored state may distinguish saving from restoring.
If the result supports neither explanation, widen the model within scope or escalate the
new dependency. A failed test may reveal an implementation fault, a faulty test/environment,
or a wrong model; investigate before choosing what to change. Preserve useful counterexamples.

After a process change, predict what should improve on the next comparable task, then check
it. Keep, revise, or revert that change based on evidence. Do not rewrite desired outcomes
to remove prediction error. Ending early or transferring unfinished work is not success.

## Optional arithmetic, not another objective

When a coarse comparison helps, retain the mnemonic:

    Action value = expected progress + useful information − cost

Each term may use 0/1/2: no/partial/direct contribution to acceptance; no/refining/action-changing
information; low/moderate/high cost. This is a rough heuristic, not calibrated arithmetic,
a probability, or expected free energy. Do not add raw seconds, tokens, and information units
as if interchangeable. If the coarse score hides the important tradeoff, discard the score
and compare the consequences directly. Prefer cheaper/reversible options when contribution
is comparable. Gates remain gates; stop optional experiments that cannot change the work.
