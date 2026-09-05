---
name: lean-quality
description: "THE single skill for executing an idea into code — use automatically EVERY time production code is written or modified: implementing a feature, fixing a bug, TDD, red-green-refactor, test-first work, or deciding what tests a change needs. Supersedes all other TDD/testing skills for automatic use (they load only by explicit name). The execution-stage discipline for turning a decided idea into verified code: TDD (red-green-refactor, three laws) as the spine; density instruments on top (property invariants, strict typing, dead-code scan, mutation score as meter); construction principles (injectable seams, determinism, fail-fast errors); never commit on red; QA-finds-nothing as the bar."
---

# lean-quality — executing an idea into verified code

Scope: the EXECUTION stage. The idea, design, and interface are already decided;
this skill governs turning them into code that provably works. It does not cover
ideation, architecture, or requirements — when those turn out to be unsettled
mid-execution, stop and resolve them first; executing an undecided design produces
confident code with a wrong spec, the one failure class no test below can catch.

## The spine: test-driven development

Everything in this skill is TDD or an extension of it. The core cycle:

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

Why the cycle is load-bearing, not ceremony: a test never seen red proves nothing
(it may pass vacuously or assert the wrong thing); code written before its test is
code whose testability was never checked; and running tests after every edit keeps
the cause of any red nameable from the last edit alone — long gaps between runs
turn a one-line diagnosis into an archaeology dig.

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
   entry points. A strict type-check is a proof over every path, including paths no
   test reaches. Keep both in the done-checklist so they cost nothing forever.

3. **Example tests where properties fit poorly:** CLI handlers, parsing of external
   tool output, error branches with specific messages. These are the classic TDD
   unit tests — few, sharp, message-exact.

4. **Mutation testing: does the suite actually constrain the code?** TDD's promise
   is that the tests pin behavior; mutation score MEASURES that promise. Run a
   probe to find what the suite would not notice; read survivors as a map of
   genuine gaps vs equivalent mutants (4–39% of survivors are unkillable in
   principle — 100% kill is explicitly NOT the target; the score is a meter, never
   a gate). A kill-count that must not drop is also the cheapest behavior-neutrality
   proof for changes claiming to be refactor-only.

## Construction principles (while the code is being written)

- **Design seams for injection.** Every external effect — subprocess, network,
  clock, randomness, filesystem-as-environment — sits behind an injectable callable
  or interface, with the real implementation as a thin default. This is not test
  ceremony; it is the property that makes TDD physically possible. Law for the test
  suite: no real subprocess, no network, no wall clock, no sleep — injected fakes
  only.
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

1. **Pin red.** Failing check first, seen failing for the right reason.
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
6. **Report honestly.** Green with counts; failures with their output verbatim;
   skipped steps named as skipped. The bar: a downstream QA pass finds NOTHING.
   QA finding a bug is a process failure to learn from — identify the missing
   check and add it — never a normal part of the workflow.

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

- [ ] Every new check was seen RED before the code made it green
- [ ] Invariants of the touched module stated and encoded as properties (or an
      explicit note why none apply)
- [ ] Strict type-check clean on the touched surface
- [ ] Dead-code scan clean (whitelist entries each carry a one-line reason)
- [ ] Example tests for the property-resistant edges, asserting exact messages and
      every refusal-reason branch
- [ ] Tests are FIRST: fast, isolated, repeatable, self-validating — no real
      subprocess/network/clock/sleep anywhere in the suite
- [ ] Full suite green and fast (bound property examples: modest max_examples, no
      wall-clock deadline) — run in full before the commit, not from memory
- [ ] For refactor/annotation-only changes: mutation kill-count did not drop
- [ ] Faked seams exercised once for real if the change touches them
- [ ] Complete diff read line by line; one intent per commit; nothing unexplained
- [ ] Committed only on green; failures and skipped steps reported verbatim
