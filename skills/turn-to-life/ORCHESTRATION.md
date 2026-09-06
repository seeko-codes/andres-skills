# Delegation: focused ownership and verified integration

Read when delegation is justified or explicitly requested. This is Turn to Life's
conditional delegated-work mode, not a second manager or another project model.
Use the agreed purpose, scope, acceptance, and stage already established by the entrypoint.
For standalone research/review, use task type and completion evidence instead of a delivery stage.

## 1. Establish the whole contract and resources

The horizontal slice H is the complete chosen goal, including integration. Map major
contributions and dependencies without specifying every distant implementation detail.
Preserve settled human decisions. Shared consequential gaps return to the human through
the established channel; independent work can continue while dependent work waits.

Apply [model-strategy](../model-strategy/SKILL.md) if available; the entrypoint's manager
capability policy is the fallback. Resolve runtime-supported controls honestly. Read
[CONTEXT.md](CONTEXT.md) before dispatch for the context ceiling, warning level, measurement,
and recovery. Carry configuration and scoped effort approval into every brief and handoff.
Include the resolved optimization priorities and remaining optional-refinement allowance;
workers share the task's allowance rather than receiving a fresh quota each.
Wayfinder stays off unless enabled; read [WAYFINDER.md](WAYFINDER.md) only in that mode.
For unsettled implementation structure, use [stages.md](doctrine/stages.md) rather than
preloading hardening checks. No new interview or architecture rewrite is implied by delegation.

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

Dispatch requires human-approved subagent effort or a covering policy. Use
[model-strategy's approval procedure](../model-strategy/SKILL.md#human-decision-on-subagent-effort)
when installed; record its scope in the brief and preserve it across handoffs.
Fallback when unavailable: propose assignment, model, supported effort choices, recommendation,
and estimated quality/time/cost tradeoff; disclose inherited or unavailable controls. Batch
proposals and wait for explicit approval unless already covered. Silence is not approval;
ask again only outside the approved scope, never silently change effort. The established
maximum-effort manager policy also covers Wayfinder-launched managers unless the user changes it.

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
verification. Follow [GIT.md](GIT.md) for commits, integration, recovery, and publication;
a local checkpoint is not acceptance evidence or authorization to publish.
Update coverage and dependencies, close completed runs, and remove only reviewed, safely
integrated temporary work. Preserve unfinished work and user changes.
Finish when the integrated result satisfies H, not when all agents merely report success.

## Human-readable operation

Read [VISIBILITY.md](VISIBILITY.md) for centralized status: goal, assignments, owners,
model/effort, context measurement, dependencies, and evidence. Explain meaningful changes
and blockers without exposing private reasoning or flooding the user with child transcripts.
The [reference shelf](REFERENCES.md) is for a concrete unresolved method/tool question;
do not load it automatically or use external research to guess human intent.
