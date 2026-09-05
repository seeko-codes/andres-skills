---
name: orchestrator
description: Evaluate whether delegation would protect the main context, then coordinate the smallest useful strong fleet when it would. Use automatically when work appears context-heavy, needs deep reading or long tool trails, has independent slices, or benefits from independent review. Do not use for simple questions, short commands, tiny edits, or brief interactive clarification.
---

# Orchestrator mode v3: the small senior fleet

The main session is the thinking organ, not a foreman over thinkers. It aims, judges
deltas, freezes contracts, and adjudicates surprises in its own window. Dispatch keeps
volume out of that window. It is an offloading mechanism, never a reason to maximize
headcount.

**The dispatch line: dispatch what compresses; keep what doesn't.** Execution compresses
losslessly ("commit landed, check green"); raw reading compresses to deltas; judgment
does not compress because a report boundary strips its relations. A consumed decision
is not an owned decision. Prefer one strong agent holding a connected problem over a
panel of weaker agents holding fragments. Good aiming makes execution bounded, but it
does not make model capability irrelevant. Use strong-tier by default for work that can still
surprise the brief; route to standard-tier only after the contract and verifier make the residue
routine; use mechanical-tier only where correctness is mechanically decidable.

The tier labels below are portable assignments, not model IDs. `model-strategy` maps
them to available models before dispatch.

## Agents are general-purpose; roles belong to briefs

Choose a general-purpose agent, then define its temporary role through the question,
input corpus, permissions, and acceptance check. "Worker", "explorer", and "reviewer"
are assignment descriptions, not a fixed roster or specialist identities. Do not force
new work into those categories or infer expertise from a profile name. An independent
review is a fresh context with a critical assignment, not a different agent species.

Model capability, read/write access, tool access, and isolation are real constraints.
Keep those explicit. Prefer the general-purpose native agent with its full available tools.

Give every agent the full toolset the active harness makes available. Do not apply
role-based tool allowlists or remove tools for a reading or review assignment. A brief can
bound the work and which files may change without disabling tools. Narrow tool access only
when the user explicitly requests it or the harness itself enforces a restriction.

## Activation gate: should this task delegate at all?

Loading the skill opens the gate; it does not force a spawn. Delegate only when the expected
main-context saved is clearly greater than the brief, report, review, and coordination context added.

Delegation usually wins when at least one substantial part of the task:

- requires deep reading or long tool trails that can return as a short evidence-backed delta;
- is a bounded implementation slice with frozen decisions and a pre-pinned check;
- is independent, write-disjoint work that does not need the main session's connected context;
- needs an independent adversarial verdict because self-review is not credible.

Keep the work in the main session when any of these dominates:

- the answer, edit, or investigation is small enough to finish without diluting judgment;
- the task is still framing, prioritization, architecture, or an unresolved tradeoff;
- the files and decisions are tightly coupled, so a report would discard useful relationships;
- the user is iterating interactively and the next answer may change the problem;
- no standing question, frozen contract, or review target can define a bounded brief;
- the result cannot compress into a short delta, verified commit, or verdict.

Use the smallest delegation that pays. One scout, worker, or reviewer is valid. Never create a fleet
merely because the skill loaded. If the gate fails, state why direct work preserves more context and
continue locally.

## Hard rules

0. **Use the active harness, not a named vendor's runner.** Tasks and safeguards are
   harness-independent. Inspect the live native dispatch schema and available models; use
   Codex subagents in Codex, Claude's agent tool in Claude, and Pi's subagent tool in Pi.
   Missing another harness's tool is not a blocker and needs no substitution approval.
   Load `model-strategy`, name the selected model and effort when exposed, and report
   inherited or unavailable metadata honestly. Do not claim registry discovery that the
   current tool cannot perform. Native runtime controls must preserve the task's boundaries.
1. **Thinking stays home.** Design, ranking, contract-freezing, delta-judging, and
   surprise adjudication are main-thread work, never dispatched. Two survivals only:
   decode dispatches (reading is volume too) and adjudication dispatches (the
   self-model's errors are invisible to itself — the orchestrator never verifies its own
   design). Neither dispatches the judgment: one dispatches the reading, the other the
   de-correlation.
2. **Every dispatch is paid for by a standing question.** Decode: an open Aim question
   plus the orchestrator's written prediction. Execution: a frozen contract plus a
   pre-pinned failing check. Adjudication: a named design at stake. A dispatch whose
   result cannot change the plan is delegation theater — don't spawn it. Fleet plans
   carry a paying-question column.
3. **Zero open decisions in an execution brief.** Classifier = rule 7: if the failing
   check can be written before dispatch, the slice is execution; if it can't, a decision
   is still hiding in it and it is aim work, whatever it looks like. Every execution
   brief carries the stop-on-undecided line (see doctrine/execute.md) verbatim.
4. **Writes happen in worktrees.** With `pi-subagents`, set `worktree: true` on each
   writing child or workflow so the package owns strict managed isolation. If the active
   dispatch tool lacks isolation, make worktree creation and the exact path part of the
   bounded worker task before any write. Main-thread non-mechanical writes also enter a
   worktree. Exception: when required gitignored artifacts exist only in the main checkout,
   those slices may run there with an explicitly bounded, disjoint write-set. A slice
   needing both surfaces is split. Worktrees merge only after review.
5. **Installed capability follows task risk, not labor price.** Apply `model-strategy`
   and print the exact agent/model/effort mapping in every fleet plan. The strong tier is the default
   for interpretive decode, connected implementation, ambiguous debugging, and
   consequential adjudication. The standard tier is for bounded execution with frozen decisions and
   strong machine checks. The mechanical tier is for exact collection or transformation only. An
   independent review context matters, but never buy de-correlation by dropping below
   the review's capability bar. Design stays in the main session.
6. **One level deep.** Subagents never delegate — a slice that needs to was cut too
   big; the fix is the orchestrator re-slicing. Every brief's BOUNDS carries the
   verbatim work-alone line (doctrine/core.md).
7. **Red precedes green.** The check exists and FAILS before the work — code slices
   write the failing test first (test + implementation in one commit); non-code slices
   name their pre-pinned acceptance instrument. A check written after the work inherits
   the work's blind spots. This rule doubles as the execution/aim classifier (rule 3).
8. **Completion = a clean commit** (or the named artifact where the surface is
   gitignored). Monitors key on committed-and-clean, never on a report file existing.
9. **Harness-native dispatch only.** Launch through the active session's agent tools.
   Do not launch another agent CLI through a shell as a substitute. Use that harness's
   tracking, messaging, completion, and cancellation controls.

## Native dispatch contract

After the gate wins, read [SUBAGENTS.md](SUBAGENTS.md). It maps the invariant task
contract to available native controls. Runtime examples apply only in their own harness;
no example makes that runtime a dependency of the work.

## The loop

1. **Aim** (main thread). Use this inquiry protocol, or `curious` if separately installed:
   ranked questions over the feature, predictions before reads, checkpoints, and a
   surprise sweep. Pre-registered gaps first. Question-form yield order: "why does this
   exist / what does it change in the system?" → "how does X relate to Y?" → "what is
   X?". Fake-inquiry guard: a question already answerable converts into a prediction,
   not a dispatch. This protocol directs inquiry; it does not replace provider reasoning effort.
2. **Decode dispatches.** Scouts only for questions with standing uncertainty; the
   brief carries the question AND the orchestrator's prediction; reports are deltas
   only (doctrine/decode.md). Never fan out scouts by subtree — that is allocation by
   position; allocate by question.
3. **Judge deltas at home; cycle.** Answers breed questions; re-Aim until a round
   generates none (**satiation**). Only then:
4. **Freeze contracts.** Types, schemas, seams, the decisions scouts surfaced — written
   to the project docs (accommodation is external or it is lost). This is v1's
   "orthogonalize before you parallelize," now gated by satiation: building before
   satiation is why fleets rework.
5. **Execution batch.** Decompose into slices that are spanning (union delivers the
   feature), independent (disjoint write-sets), and vertical (end-to-end units, never
   layers). Size each slice to the active runner's context budget, leaving room for
   execution and verification. Dependencies → topological batches, and within a
   batch dispatch in **importance order** so budget death still lands the load-bearing
   work. Concentrate where element interactivity is high: one strong-tier agent per interactive
   core, never a committee. Hand frozen, local residue to standard-tier. Fan out mechanical-tier only for
   mechanically checked residue. The agent count is decided by interactivity, not by
   available parallelism. A slice boundary through connected work converts free
   in-context relations into lossy briefs.
6. **Review by surprise.** The brief's DONE condition is the prediction; review effort
   routes to deviation, not uniformly. Fully-predicted report → coverage-pointer merge.
   Surprise or contradiction → the valuable thing: adjudicate it, and write the
   accommodation into the docs. Failed work goes back to a subagent, never into the
   main thread's own hands.
7. **Batch boundary.** Merge; verify the *composed* result (spanning doesn't guarantee
   composition); run the **surprise sweep** — what did no slice claim? — and, on
   expensive batches, the breaching pass: cross-map each slice's change against the
   concerns of slices it is NOT connected to; composition bugs are unknown gaps.
   Adjudication dispatches run here, de-correlated by assigned lens
   (doctrine/adjudicate.md); verification is deliberately redundant — the
   no-redundancy rule binds construction only. Then prune: merged worktrees and
   branches die the day they merge.
8. **Reflect and hand off.** One-experiment Kolb's pass (below), close the ledgers,
   write the successor block — next batch's slices, fleet plan, gates, plus decisions
   made AND why the alternatives lost — then report the completed batch. Offer a fresh session when context pressure makes
   it useful, using the active runner's supported controls. Never require a runner-specific
   command or invite a reset while children are still running.

## Briefs

Before writing any child task, read [BRIEFS.md](BRIEFS.md) and the matching doctrine file. Briefs
carry only the bounded corpus, authority, DONE check, and compressed report contract that child needs.

## Monitors — cue → monitor → respond

- **Dispatches-without-crystallization**: N dispatch rounds without a settled decision
  means the fault is upstream — re-Aim or re-slice; never spawn more agents.
- **Executor-capability mismatch**: if a standard-tier slice encounters interpretation,
  cross-system coupling, or an incomplete contract, stop it. Pull the decision back to
  Aim or reroute the now-understood connected slice to strong-tier. Never compensate with more
  standard-tier agents or mechanical-tier at higher effort.
- **Burn-rate**: budget fraction outrunning finished-slice fraction → re-rank remaining
  slices by importance (graceful degradation).
- **Efficiency = decisions-settled ÷ tokens-spent** — never agents-spawned, never
  coverage. Each fleet-plan line names the question that pays for that agent.

## Kolb's layer — one experiment per batch

After each batch, one reflection pass over what the batch actually cost and settled;
propose one evidence-backed improvement to test in the next batch. Changes to installed
skills require the user's authorization; reflection alone does not authorize rewriting them.

**Quality-first batch experiment:** compare the small, strong-tier-heavy fleet against the last
comparable batch. Pin escaped defects, rework batches, decisions reopened after merge,
and composed-check failures before dispatch. Agent count and token use are diagnostics,
not the objective. If standard-tier performs equally on a frozen task with strong checks, keep
that routing. If quality differs or the task lacks a reliable verifier, route upward.

## Exceptions

Answering questions, small scoped code reads, git operations, short read-only commands, and
mechanical edits (doc moves, pointer edits, appends, config values, handoff upkeep) are main-thread
work. Deep reading becomes a decode candidate only when its volume would crowd out judgment and
its answer compresses cleanly. Do not delegate a one-line answer. These rules guard feature
implementation and window hygiene, not conversation or upkeep.
