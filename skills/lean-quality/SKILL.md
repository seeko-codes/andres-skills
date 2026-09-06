---
name: lean-quality
description: Harden a coherent implementation with proportionate behavior, integration, and visual verification. Use for settled implementation or prototype promotion; defer full hardening while the arrangement is uncertain.
---

# Lean quality

## Choose the stage

Explore while responsibilities, interfaces, or user flow remain uncertain. Use the smallest
experiment that answers the consequential question, including early security, performance,
or integration checks when feasibility depends on them. Preserve project protections.
Do not automatically impose full hardening on an exploratory prototype.

Harden a bounded scope once its responsibilities, critical connections, expected behavior,
and acceptance criteria are coherent and supported by evidence. Distant work may still be
exploratory. If a structural assumption fails, return the affected scope to exploration.
Explicit user requests for test-driven development or this skill still apply.

## Retain and verify

Inventory prototype shortcuts and decide what to keep, refactor, replace, or discard.
Derive expected behavior from the agreed contract, independently of the implementation.
Characterization tests for existing code may initially pass; label them as post-hoc evidence.
Do not delete working code or manufacture failures to claim retrospective TDD.

For new behavior and bug fixes, use red-green-refactor: observe a test failing for the
intended reason, implement the behavior, then improve structure while preserving behavior.
For a bug, the test should reach the actual failure pattern. If the environment prevents
reproduction or verification, report the specific gap rather than claim a verified fix.
Tests should constrain observable contracts so a slice can be replaced without rewriting
tests merely to match new internals. Assert exact wording only when wording is contractual.

## Select checks from the actual risk

Use existing project tools and required gates. Choose additional checks for concrete
failure modes, rather than requiring every tool for every change:

- **Behavior tests:** important outcomes, boundary conditions, and relevant failure paths.
  Use property-based testing when an invariant over inputs or sequences is useful.
- **Static analysis:** relevant build, type, lint, or dead-code checks supported by the project.
  Do not impose a new strictness migration or tool installation as incidental cleanup.
- **Integration:** exercise changed connections with controlled real implementations where
  possible. Test doubles can isolate unit behavior but cannot establish that integration works.
- **Visual verification:** for UI changes, try the relevant interactions and inspect screenshots
  of meaningful states and viewports. Appearance alone does not verify functionality.
- **Fault sensitivity:** use a negative control or targeted mutation when there is a concrete
  question about whether a critical test would detect a fault. Investigate surviving mutants;
  equivalent mutants are not missing behavior. Raw kill-count is not a cross-version gate.

Preserve discovered failing inputs as regression evidence. Keep experimental mutation runs
isolated from the working implementation and its test data; do not wipe useful examples.
Keep nondeterminism controlled where possible and distinguish flaky checks from product defects.

Run affected checks during iteration. Broaden verification for integration risk, relevant
failures, or project-required gates. Stop when acceptance and those gates are sufficiently
verified; do not repeat a full suite solely because another checkpoint commit is being made.
Do not invent behavioral tests for documentation-only or trivial reversible edits.

## Completion

Inspect the actual change and integrated result against acceptance. Report what was checked,
the results, and material remaining uncertainty. A checkpoint may preserve incomplete work;
label it accordingly. Production-ready claims require the scoped checks and mandatory gates
to pass. No test suite, mutation score, or review guarantees zero defects or complete security.

Use canonical terms in technical records. Explain human-facing work through actions, purpose,
and evidence. For a concrete unresolved method/tool question, consult
[REFERENCES.md](REFERENCES.md) on demand; do not preload its sources.
