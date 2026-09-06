---
name: orchestrator
description: Manage context-heavy work through breadth-first planning, dependency-ordered batches, and a small capable team with focused contracts. Use when delegation materially protects context, creates useful specialization, or enables parallel work; keep small tasks local.
---

# Orchestrator: broad understanding, focused execution

Context management is the objective. Decomposition allocates work, intelligence, and
context together. Prefer fewer, smarter, autonomous agents with meaningful ownership.
The manager holds the global picture and compiles it into locally complete assignments;
workers need depth on their contracts, not the entire project history.

The durable project model explains how the software fits together; this skill compiles
its relevant relationships into temporary assignments and integrates their evidence back
into the project. Keep these lifetimes separate so a new task need not reconstruct the
whole repository, and a repository module need not become a permanent agent assignment.

## Manager and configuration

Use the smartest available model at the highest supported reasoning effort for the manager.
Resolve capabilities from the active runtime; if the current session cannot be upgraded,
report its actual settings and limitation. Never claim a model or effort change that did not occur.
Subagents may match the manager or use less capability and effort when sufficient.
Use `model-strategy` if installed; otherwise choose from complexity, consequence, and verifier
strength. Cheap execution is appropriate only when the remaining work supports it.

Resolve these user-overridable settings once and carry them into every brief and handoff:

| Setting | Default | Meaning |
|---|---|---|
| `max_context_per_agent` | `100000` tokens | Assignment context ceiling, including every manager and worker |
| `context_warning_fraction` | `0.8` | Start checkpointing/replanning at this fraction of the ceiling |
| `wayfinder` | `false` | Optional continuity manager above orchestrators |

Use the lower of the configured ceiling and the runtime's supported context limit.
Read [CONTEXT.md](CONTEXT.md) before dispatch for measurement and recovery rules.
Read [WAYFINDER.md](WAYFINDER.md) only when Wayfinder mode is enabled.

## 1. Define the horizontal goal; think breadth first

The horizontal slice H is the complete chosen goal. Establish deliverables, constraints,
exclusions, and integrated acceptance criteria before dispatch. Map the major work and
its dependencies broadly; do not exhaustively specify distant implementation details.
The human owns highest-level direction and consequential unresolved tradeoffs.
Investigate resolvable uncertainty; bring genuine decision gaps with options, evidence,
and a recommendation. For unresolved project purpose, scope, priorities, or domain meaning,
use `grill-with-docs` when installed; otherwise ask one focused question at a time and record
the human's decision. The agent may reason about intent but cannot choose the user's goals
on their behalf. Resume dependent work once that decision is sufficiently clear; independent
work can continue. Existing authorization persists; do not reopen settled choices or ask the
human to manage routine handoffs.

## Use reusable architecture when structure is at issue

When building or revising project responsibilities, interfaces, or navigation, use
[context-architecture](../context-architecture/SKILL.md) when available. It owns the reusable
problem-solving backbone; this skill owns stages, work slicing, resources, and integration.
Use its relevant relationships and locators to form locally complete contracts, not one
agent per module. Keep small work local and existing approvals intact. When a boundary is
unclear, consult its [workflow contract](../context-architecture/WORKFLOW.md); do not preload
unrelated dependencies. If unavailable, use existing project architecture evidence.

## Establish coherence before hardening

Use exploration while the feature arrangement, interfaces, or user flow remain uncertain.
Map alternatives broadly, then commission bounded prototypes or spikes to answer specific
questions. Read [stages.md](doctrine/stages.md) when implementation direction is unsettled.
Do not load `lean-quality` or run its full checklist during exploration unless explicitly
requested. Keep baseline checks that make the experiment trustworthy and preserve existing
project protections. A working prototype is evidence about the design, not production completion.

Once the current scope has coherent responsibilities, exercised seams, settled acceptance,
and no unresolved structural decision that would invalidate its construction, record that
basis and enter hardening. Apply `lean-quality` to retained code, with TDD for new behavior
and fixes plus integration and visual checks where relevant. Distant batches may remain
exploratory; hardening applies to a coherent bounded scope, not only to an entire finished project.

## 2. Decompose into vertical slices and batches

A vertical slice is a cohesive, independently checkable contribution. The basis-vector
analogy means collective coverage and independent construction, not literal vector algebra:

- Across all batches, the union of slice deliverables equals H. Include integration work.
- Concurrent writing slices have disjoint write-sets. Shared reading and shared constraints are valid.
- Concurrent slices have no unresolved dependency on each other's unfinished outputs or decisions.
- Extract shared interfaces, schemas, and decisions into prerequisite work before dependent slices.

A batch is a ready set of independent slices; queue dependent batches behind verified
prerequisites. One batch need only cover its intermediate scope. The complete sequence
must cover H. Specify the current batch precisely and refine future batches after integration.
Re-slice oversized contributions relative to their own deliverable. Keep connected work
with one capable owner when splitting would create more coordination than it saves.

Keep decisions that change together within one slice. Other slices should need its
contract, not its internal choices. Vertical slices should be easy to replace.

## 3. Allocate capability and contract-specific context

Delegate only when specialization, context protection, or parallelism justifies briefing,
reporting, and review costs. Parallelism is a benefit, not a headcount target.
Difficult reasoning may go to an equally capable agent; the manager owns adjudication
and the cross-slice implications. Workers have autonomy over local decisions within their contracts.

Read [BRIEFS.md](BRIEFS.md) before dispatch. Give each worker exact requirements, relevant
sources, dependency outputs, applicable constraints, and acceptance checks. Translate
necessary global decisions into local constraints and concise rationale. Exclude unrelated
features, conversations, and historical debate. Focused context supplies knowledge;
model capability still determines whether the agent can use it well.

Before dispatch, propose subagent reasoning effort to the human with the assignment,
selected model, supported effort choices, recommendation, and expected quality/time/cost
tradeoff (label estimates). Group proposals by batch. Wait for the human's choice or approval
unless an existing user-approved effort policy already covers the assignment. Silence is not
approval. Record the scope of that approval in the brief and carry it through handoffs;
ask again only for assignments or changes outside that scope. Do not silently raise or lower
effort. If effort is inherited or unavailable, explain the actual control limitation before
approval; do not promise an unsupported setting. The established maximum-effort manager
policy also covers Wayfinder-launched managers unless the user changes it.

## 4. Dispatch, observe, and adjust

Read [SUBAGENTS.md](SUBAGENTS.md) for the active runtime. Use native tracked agents and
isolated worktrees for writing tasks where applicable. Record exact ownership and paths.
Workers cannot delegate. Orchestrators cannot spawn more managers. The sole exception
is an enabled Wayfinder, which may launch orchestrators authorized to launch workers.

Monitor context consumption; do not wait for a worker to declare its task too large.
Crossing the configured ceiling means the assignment was oversized for its budget.
Preserve progress, stop further growth, and re-slice or hand off the remaining work.
Missing requirements, shared contract changes, or ownership collisions return to the manager;
routine choices inside the contract stay with the worker.
If slices repeatedly need one another's unfinished reasoning or manager mediation,
reconsider the boundary: combine the coupled work or resolve its shared decision first.
Investigate the cause rather than automatically merging assignments; a missing requirement
can produce the same symptom. Any revised effort assignment follows the human approval rule.

## 5. Verify, integrate, and continue

Require output locations, acceptance evidence, consequential rationale, deviations, and
remaining uncertainty. Reports are compressed evidence, not raw working histories.
Follow the matching [research](doctrine/decode.md), [execution](doctrine/execute.md), or
[review](doctrine/adjudicate.md) guidance only for that assignment.

Verify individual contracts, then integrate accepted outputs and verify their composition.
Risk and uncertainty determine independent review needs. Matching expectations is not
verification. A clean commit records completion; it does not prove correctness.
Update coverage and dependencies, close completed runs, and remove only reviewed, safely
integrated temporary work. Preserve unfinished work and user changes.
Finish when the integrated result satisfies H, not when all agents merely report success.

## Human-readable operation

Read [VISIBILITY.md](VISIBILITY.md) when planning or running delegated work. Centralize
status so the human can see the goal, sequence, each assignment's purpose, model/effort,
context usage, dependencies, and status. Explain what is happening and why at planning,
dispatch, blockers, changed decisions, verification, integration, and handoff; provide
periodic updates during long work. Expose concise rationale and evidence, never private
chain of thought. Do not drown the manager or human in every child tool call. If an explanation does not land,
restate its context, action, and purpose plainly; honor an explicit `wait-what` invocation
when that skill is installed.

## Terminology, explanation, and ambiguity

Use canonical technical terminology in agent instructions, contracts, and technical
records. In human-facing updates, explain the action, purpose, evidence, and decision in
familiar language; introduce a technical term only when useful and explain it briefly.
For an unresolved method or tool question, consult [REFERENCES.md](REFERENCES.md) on demand.
Do not load the shelf or its sources automatically, and do not use external research to
guess the human's intent.
