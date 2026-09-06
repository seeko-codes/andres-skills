# Explore, establish coherence, then harden

Breadth-first planning determines what belongs together and what depends on what. Focused
experiments can go deep enough to resolve a structural uncertainty. Hardening is a later
quality stage, not a competing search algorithm. Use the stage appropriate to each bounded scope.

Information-gathering and implementation are actions, not stage labels. Either may occur
within either stage. A context-architecture action score cannot replace the coherence gate
or required checks; a local uncertainty does not automatically reopen the whole project.

## Exploration

After mapping the goal broadly, test the unresolved assumption most likely to invalidate
substantial downstream work. Use the smallest experiment that can inform the decision.
Defer exhaustive hardening, but bring forward a security, performance, or integration check
when its result determines whether the arrangement is viable.

When arrangement is uncertain, name the question, candidate approaches, evidence required,
and stopping condition. Build the smallest useful prototype or vertical skeleton; try another
approach when findings justify it. A contract may commission an experiment rather than freeze
an implementation architecture. Preserve write ownership, context limits, and shared constraints.

Do not automatically load lean-quality or impose exhaustive hardening checks. Run what makes the experiment credible: a build or targeted check, a real interaction,
a narrow integration probe, or screenshots of relevant UI states. Tests are useful during
exploration when they answer the uncertainty; they are not a universal entry toll. Preserve
existing mandatory checks and data/access protections. Use isolated work and reversible effects.
Label prototype commits and deferred quality work. A checkpoint can preserve incomplete work;
it is not approval to release or a claim that the goal is complete.

## Coherence gate

Before hardening the selected scope, the manager records evidence that:

- Responsibilities and dependencies form a plausible whole; important seams were exercised.
- The proposed user flow or behavior addresses the horizontal goal and acceptance criteria.
- Alternatives that materially affect structure have been considered or tested.
- No unresolved structural decision is likely to invalidate the implementation being hardened.

Use evidence, not merely 'looks coherent.' Resolve consequential uncertain choices with the
human; routine transitions need no new permission. State what was chosen and why. Do not wait
for all distant work to be designed. An already settled bug fix or feature goes directly to hardening.

## Hardening and promotion

Load lean-quality for retained code. Inventory prototype shortcuts and choose what to keep,
refactor, replace, or discard. Tests must derive from agreed behavior, not reproduce accidental
prototype details. Characterization tests may initially pass; label them as post-hoc evidence.
Use red-green-refactor for new behavior, discovered gaps and fixes. Do not delete working code
or invent failures merely to claim retrospective TDD. Check that key tests can detect relevant
faults with an appropriate negative control or targeted mutation when useful.

For UI, exercise real interactions and capture/inspect relevant viewport and state screenshots.
Screenshots show appearance; they do not establish interaction, accessibility, backend, or
security correctness. Combine them with checks of the behavior and seams actually at risk.
A reference or approved screenshot is a comparison target only when one exists.

Complete scoped quality and integrated acceptance checks before promotion to production-ready.
Report remaining limitations; hardening cannot promise complete security or zero defects.
If structural evidence fails, return the affected scope to exploration and preserve valid work.
