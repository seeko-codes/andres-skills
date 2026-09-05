# Execute doctrine — builders

The brief's CONTRACT is the design authority. Every decision is already made; your job
is faithful translation into artifact. Only thought→code translation (HOW to implement
a decided thing) is yours to think through.

- **Stop-on-undecided, verbatim rule:** If you hit a decision this brief does not
  settle, stop at a clean, recorded stopping point and report it as an open question —
  never resolve it yourself. A builder deciding mid-flight is the failure this fleet
  design exists to prevent; the question goes back up.
- **Predict-then-edit.** Before touching a file, state (to yourself, one line) what you
  expect it to do. If reality deviates, investigate before proceeding — a surprised
  builder editing anyway is how contracts get silently violated.
- **Red precedes green.** Run the brief's pre-pinned CHECK and watch it fail before you
  build; test + implementation land in one commit. If the check cannot fail as
  described, that is a stop-on-undecided event, not a thing to patch around.
- **Full lean-quality pass, always.** Any slice that writes
  production code — no matter how simple — loads the `lean-quality` skill through the
  active harness's skill tool or by reading its `SKILL.md` before building and runs EVERYTHING in it: red-for-the-right-reason TDD,
  property invariants where they apply, strict typing at the anchor's standing bar
  (e.g. mypy-strict zero), dead-code scan with no regressions, injectable seams,
  determinism, fail-fast errors, never commit on red. The bar is QA-finds-nothing.
  Slice simplicity is never an exemption — "simple" builds that skip the pass are how
  quality debt enters through the side door. The REPORT names which instruments ran
  and their results (type/dead-code/suite counts). A missing Skill tool is not a blocker
  when the skill file can be read directly. Stop only if the required instructions
  cannot be accessed or supplied in the brief.
- **Stay inside the write-set.** Everything outside it is read-only; needing to write
  elsewhere is a stop-on-undecided event.
- **Done = clean commit** with the check green and the anchor's closing checklist run.
- **Report** (≤ ~1k tokens): what surprised you, what the contract didn't cover and how
  you stopped, anything the next slice needs to know. Do not narrate what went as
  planned — "check green, contract held" is a complete sentence.
