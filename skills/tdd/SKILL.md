---
name: tdd
description: Apply test-driven development when explicitly requested, including /tdd. Automatic hardening of coherent implementation is handled by lean-quality.
---

# Test-driven development

This skill makes behavioral expectations answerable to executable evidence, one change
at a time. Receive the agreed contract and explicit method request; return test-first
implementation evidence within the current delivery stage. The tests constrain behavior,
not the repository model's preferred explanation or folder layout.

Use this method within the user's agreed scope. Reuse established requirements and approvals;
ask only about unresolved intent, consequential interface choices, or missing acceptance.
Do not turn routine test selection into another approval round. Subagent effort decisions
still follow the user's effort-approval policy.

List the desired behaviors broadly, then implement one behavior at a time:

1. **Red:** write a focused test and observe it fail for the intended missing behavior.
2. **Green:** implement enough to satisfy that behavior and check for regressions.
3. **Refactor:** improve structure with behavior checks passing before and after.

Repeat using what each cycle reveals. Planning the behavior list first is useful; implementing
all tests before any feedback from code can lock in premature assumptions. This test-first
batching issue is distinct from the orchestrator's horizontal slice, which means the whole goal.

Test observable contracts through appropriate interfaces. Prefer checks that remain valid
when an implementation is replaced. A call count, database observation, or exact error message
is appropriate when it is part of the actual contract; otherwise avoid coupling to internals.
Use test doubles to control relevant boundaries and real integration checks for the connections
they replace. Choose test scope from the failure being investigated.

Existing working code can use characterization tests that initially pass. They are not
retroactive TDD; do not manufacture a failure history. A missing reproduction or unavailable
environment is a verification limitation to report, not evidence that the fix works.

Exploratory work remains exploratory even when the user requests TDD for an experiment.
Do not infer that using this method requires the full lean-quality hardening stage.

Read supporting guidance only for a question that needs it:
[tests](tests.md), [test doubles](mocking.md), [interfaces](interface-design.md),
[module boundaries](deep-modules.md), or [refactoring](refactoring.md).
For an unresolved external definition or workflow, use [REFERENCES.md](REFERENCES.md)
on demand. Explain the action and purpose plainly to the human; keep canonical terms in
technical records.
