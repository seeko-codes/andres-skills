---
name: lean-quality
description: "Harden a coherent implementation with TDD, behavior and property checks, static analysis, integration evidence, and visual verification where relevant. Use automatically for settled implementation and prototype promotion, or on explicit request. Defer during uncertain architecture, arrangement experiments, and exploratory prototypes."
---

# lean-quality — executing an idea into verified code

## Activation: coherence before hardening

This is the HARDENING stage. Do not automatically run this skill during early exploration
of architecture, feature arrangement, or user flow. During exploration use focused experiments
and baseline checks sufficient to trust the findings; preserve project protections. Explicit
user requests for lean-quality or TDD still apply.

Enter when the selected scope has coherent responsibilities and interfaces, exercised critical
seams, agreed behavior and acceptance, and no unresolved structural question likely to invalidate
its implementation. This need not wait for the entire project. An already understood bug fix
or settled feature can enter directly. Workers retain local implementation autonomy; escalate
cross-slice changes. If structural uncertainty reopens, return that scope to exploration.

## Bringing a prototype into hardening

Inventory retained code, shortcuts, and deferred checks. Keep, refactor, replace, or discard
based on the agreed contract. Characterization tests for existing behavior may initially pass;
report them as post-hoc tests, not TDD. Derive expected results from requirements rather than
copying the prototype. Where useful, use a negative control or targeted mutation to check that
a critical test can detect a relevant fault. Do not manufacture failures or delete working code
to satisfy test-first history. Apply the cycle below to new behavior, gaps and fixes, then refactor
retained code under verified checks. Full hardening and integrated acceptance precede production
completion; an exploratory checkpoint is not a release-ready claim.

## The spine: test-driven development

For new behavior and fixes, use the following cycle. Existing prototype characterization
follows the explicit transition above:

- **Red** — write the smallest test that fails for the right reason, and RUN it to
  see the failure. The three laws: (1) no production code except to pass a failing
  test; (2) no more of a test than suffices to fail — a compile/import error is a
  failure; (3) no more production code than suffices to pass. Bug fixes obey the
  same law: reproduce the bug as a failing test before touching the code.
- **Green** — the least code that passes. Resist generalizing beyond what the tests
  force; the next test earns the next increment of generality.
- **Refactor** — with the suite green before AND after, in steps small enough to
  revert freely. This is where duplication is removed, names are improved, and
  structure emerges. Skipping this step is how green code rots.

Observing the intended failure helps establish that a new test detects the missing behavior.
A passing post-hoc test can still supply evidence; its limits and fault sensitivity must be
assessed honestly. Keep iterations small enough to diagnose failures and revise the design.

**Test quality is code quality.** Tests are first-class code held to FIRST:
Fast (milliseconds — a slow suite stops being run, and an unrun suite is no suite),
Isolated (no ordering or shared state between tests), Repeatable (same result on
any machine, any time — see Determinism below), Self-validating (pass/fail, no
human inspection of output), Timely (written with the code, not after). Structure
each test as arrange-act-assert, one behavior per test, named for the rule it
pins ("gate rejection never mutates the plan"), not the method it calls.

## The instruments: density over transcription

Classic TDD grows example tests one at a time. Keep that cycle, but ship assurance
as a small stack of DENSE instruments rather than transcribing dozens of examples.
Each instrument is TDD's idea — executable statements about the code that a machine
checks — at a different altitude:

1. **Properties: TDD over generated inputs.** One property-based test file
   (Hypothesis or equivalent) encoding the module's *invariants* — laws that hold
   for any legal input or call sequence: "state X is unreachable without step Y",
   "a rejected operation never mutates persisted state", "parse(serialize(x)) == x",
   "any schema-complete input parses; any incomplete input rejects". Use a
   stateful/rule-based machine when the invariant is about sequences. One property
   replaces dozens of hand-picked examples AND the examples nobody thought to pick.
   Fold cheap high-value checks in as one-line asserts (immutability of value
   types, boundary tables, sequence monotonicity, error-on-unknown-input).

2. **Strict types + dead-code scan: tests the compiler runs.** `mypy --strict` (or
   the language's strictest checker) and `vulture`-class dead-code detection on the
   changed surface, kept at ZERO findings via fixes or a *documented* whitelist —
   one line of justification per retained name; never delete deliberately-deferred
   entry points. A strict type-check checks static constraints beyond sampled tests; it does not
   prove runtime behavior or specification correctness. Keep both in the done-checklist so they cost nothing forever.

3. **Example tests where properties fit poorly:** CLI handlers, parsing of external
   tool output, error branches with specific messages. These are the classic TDD
   unit tests — few, sharp, message-exact.

4. **Mutation testing: does the suite actually constrain the code?** TDD's promise
   is that the tests pin behavior; mutation score MEASURES that promise. Run a
   probe to find what the suite would not notice; read survivors as a map of
   genuine gaps vs equivalent mutants (4–39% of survivors are unkillable in
   principle — 100% kill is explicitly NOT the target; the score is a meter, never
   a gate). A nondecreasing kill-count is a regression signal for changes claiming to be
   refactor-only; it is not proof of behavior neutrality.

## Construction principles (while the code is being written)

- **Design seams for injection.** Every external effect — subprocess, network,
  clock, randomness, filesystem-as-environment — sits behind an injectable callable
  or interface, with the real implementation as a thin default. This is not test
  ceremony; it is the property that makes TDD physically possible. Keep unit tests deterministic with injected fakes. Separately exercise relevant
  real seams with controlled integration and smoke tests.
- **Determinism by construction.** Core logic never reads the clock or a random
  source directly; time and randomness enter as parameters. This is what makes
  tests Repeatable and runs replayable.
- **Fail fast, loud, and specific.** Validate at boundaries and raise immediately;
  never swallow an exception or return a silent default for a broken invariant.
  Error messages name the violated rule and the offending value — and tests assert
  those exact messages and each refusal-reason branch alone and combined. A test
  that checks only "it raised" kills nothing inside the raise path.
- **Small units, honest names.** Functions do one thing at one level of abstraction;
  names say what the caller gets, not how. Readability is a correctness tool: code
  that can be read can be reviewed, and review is the only instrument that catches
  code-and-tests-wrong-together.
- **Duplication is removed in the refactor step, not prevented in the green step.**
  Write the duplicate, get green, then extract — premature abstraction under red is
  how wrong interfaces calcify.
- **Comments state constraints the code cannot express** (protocol invariants,
  "split on \n only because upstream emits U+2028", sanctioned exceptions) — never
  narration of what the next line does.
- **One intent per commit.** Small commits whose message states the intent; a
  reviewer should be able to hold the whole diff. Mixed refactor+behavior commits
  hide behavior changes inside noise.

## The execution loop, end to end

1. **Establish the check.** For new behavior/fixes, observe the intended failure first.
   For retained prototype behavior, establish honest characterization coverage as described above.
2. **Go green small.** Least code; run affected tests after every edit.
3. **Refactor under green.** Boy-Scout the touched surface — cleaner than found,
   but scoped: never a drive-by rewrite of code the change doesn't own.
4. **Never commit on red — and never on unknown.** Unrun tests and unread tool
   output count as red. Pre-commit ritual: FULL suite, strict type-check, dead-code
   scan, and the complete diff read line by line — no debug leftovers, no dead
   code, no accidental file, nothing you cannot explain.
5. **Prove it runs.** Tests exercise what tests reach. If the change touches a seam
   the tests fake, run the real thing once (smoke run, live invocation) before
   calling it done. "All tests green" on an unexercised seam is a statement about
   the fakes, not the code.
6. **Inspect visual behavior when relevant.** For UI changes, exercise interactions and
   capture/inspect screenshots at relevant states and viewports. Compare with requirements
   and an approved reference if available. Screenshots do not replace behavioral, accessibility,
   integration, or security checks appropriate to the change.
7. **Report honestly.** Green with counts, failures with evidence, skipped steps and remaining
   limitations named. Learn from later defects by identifying the missing check. Passing this
   process does not guarantee complete security or the absence of defects.

## Discipline that keeps the instruments trustworthy

- **Generators must match the code's semantics.** If the code strips input,
  generate strip-stable text; if "complete" means non-blank-after-strip, filter the
  generator accordingly. A generator looser than the spec produces false failures;
  tighter produces false confidence.
- **A property failure found late is still a finding.** Repeated suite runs
  (mutation probes, CI retries) give the generator far more draws than local runs —
  rare inputs WILL eventually appear. On a property failure, first re-run on the
  clean tree: decide code bug vs generator bug vs example-database replay before
  trusting any run that followed it.
- **Isolate probe runs.** Wipe the property-test example database (e.g.
  `.hypothesis/`) before every mutant run, or saved failing examples from one
  mutant falsely kill all later mutants — and poison the clean tree.
- **Pin property-found bugs twice.** Fix the code, add a *deterministic* regression
  test with the concrete failing input, then widen the generator back so generation
  keeps covering the fixed class.
- **Known blind spots — no score or suite can see:** code and tests wrong together
  (only independent review or regeneration catches it), code that never runs (only
  a live run catches it), and equivalent mutants (noise). Never present green — or
  a good kill score — as sufficiency.

## Done-checklist for a code change

- [ ] Selected scope passed the coherence gate; retained prototype shortcuts are resolved
- [ ] New behavior/fix tests were seen RED before implementation; prototype characterization
      is explicitly post-hoc and checked for relevant fault sensitivity
- [ ] Invariants of the touched module stated and encoded as properties (or an
      explicit note why none apply)
- [ ] Strict type-check clean on the touched surface
- [ ] Dead-code scan clean (whitelist entries each carry a one-line reason)
- [ ] Example tests for the property-resistant edges, asserting exact messages and
      every refusal-reason branch
- [ ] Unit tests are FIRST and deterministic; controlled integration tests cover relevant real seams
- [ ] Full suite green and fast (bound property examples: modest max_examples, no
      wall-clock deadline) — run in full before the commit, not from memory
- [ ] For refactor/annotation-only changes: mutation kill-count did not drop
- [ ] Faked seams exercised once for real if the change touches them
- [ ] For UI changes, relevant interactions and screenshots inspected; visual checks do not
      substitute for behavior or other applicable acceptance criteria
- [ ] Complete diff read line by line; one intent per commit; nothing unexplained
- [ ] Committed only on green; failures and skipped steps reported verbatim
