# The logic of the collection

This is the repository-wide explanation, not another execution checklist. Read it when
understanding or changing how the skills fit together. For a specific task, start with
the relevant skill in the [README](README.md#the-skills); do not preload this document.

## The shared problem

We want agents to solve human problems through software without each new feature forcing
the next agent to reconstruct the whole project. Correct software is the outcome;
context-efficient understanding is one means of reaching and maintaining it.

Two kinds of structure help with different parts of that problem:

- **Reusable project structure:** the responsibilities, contracts, relationships, and
  locators that explain the software across tasks and sessions.
- **Temporary work structure:** the current goal, assignments, owners, evidence, and
  integration sequence needed to deliver one change.

The first belongs to context architecture. The second belongs to orchestration. Combining
them into one large skill would couple a durable model of the project to every temporary
execution choice. Separating them without a shared contract would produce well-organized
files and workers that still lack the relationships necessary to use them.

The collection connects them through existing project artifacts and scoped briefs.

## Build understanding before adding detail

The construction order is **problem → solution logic → concepts → details**:

1. The problem supplies purpose, constraints, and observable success.
2. The logic explains why the solution's main responsibilities are necessary and how they interact.
3. Concepts make those relationships concrete as responsibilities and interfaces.
4. Implementation details realize those responsibilities in code, tests, configuration, and other files.

This is an order of understanding, not four required directories or a demand for a complete
upfront design. Begin with enough structure for the next useful detail; let implementation
and experiments expose where the structure needs correction. A processing sequence can
explain behavior without dictating module boundaries. Good boundaries also consider what
changes together and which internal decisions callers should not need to understand.

The intended payoff is specific: for an unfamiliar task, the backbone helps an agent
predict the relevant responsibility, its necessary supporting relationships, and the
implementation detail that can remain unopened. Names and locators connect that reasoning
to actual code. A hierarchy that merely labels topics does not establish this benefit.

For example, an app chooses practice from current learner evidence. Evaluation updates
that evidence. If practice ignores a new answer, these relationships suggest inspecting
selection and evidence updates, not every screen. That route remains a hypothesis; an
unexpected dependency can require inspecting another branch.

See [context architecture](skills/context-architecture/SKILL.md) for the construction method.

## How each skill earns its place

These boundaries are chosen by the decision each skill owns, not by a desire for more skills.
The human owns project purpose and consequential tradeoffs throughout.

| Skill | Why it exists | Receives | Returns | Does not own |
|---|---|---|---|---|
| [grill-with-docs](skills/grill-with-docs/SKILL.md) | More code cannot resolve an unmade human decision | Current goals, evidence, and a consequential ambiguity | A recorded human decision and remaining uncertainty | The human's desired outcome or routine implementation choices |
| [context-architecture](skills/context-architecture/SKILL.md) | More files should not require more unrelated reading | Agreed purpose and evidence about the project | A revisable backbone, meaningful boundaries, locators, and routing evidence | Dispatch, effort approval, or delivery-stage gates |
| [orchestrator](skills/orchestrator/SKILL.md) | Large work needs bounded responsibility and verified integration | Agreed outcome and relevant project relationships | Contracts, ready batches when useful, integrated results, and accepted model revisions | The human's goals or another skill's verification method |
| [model-strategy](skills/model-strategy/SKILL.md) | A narrow context does not make difficult judgment easy | A bounded contract, remaining uncertainty, consequences, and verifier strength | A supported capability recommendation and human-approved effort selection | Scope, extra workers, or silent effort changes |
| [lean-quality](skills/lean-quality/SKILL.md) | A plausible implementation is not evidence of correctness | Coherent behavior, interfaces, acceptance, and concrete risks | Scoped verification and explicit remaining limitations | Product intent or proof that every possible defect is absent |
| [tdd](skills/tdd/SKILL.md) | Test-first development needs a tight behavioral feedback loop | Agreed behavior and an explicit request for the method | Failing-then-passing evidence and refactored implementation | The project's delivery stage or unrelated testing mandates |
| [wait-what](skills/wait-what/SKILL.md) | An explanation the human cannot follow cannot support informed direction | An explicit request to explain again | A clearer account with the missing background | Redesigning the project or silently changing its decisions |

The dedicated TDD skill has an explicit trigger. Separately, lean-quality already calls
for red-green-refactor for new behavior and fixes during applicable hardening. Explaining
these roles does not create or remove a testing requirement. Higher-priority instructions
and explicit user direction still govern.

`wait-what` is a verbatim third-party skill. Its collection role is explained here and in
its [collection-maintained companion](skills/wait-what/REFERENCES.md), not by rewriting
its upstream instructions. Its [notice](skills/wait-what/NOTICE.md) and license remain intact.

## One loop, not a mandatory procession through every skill

The central relationship is:

**Human intent → project backbone → scoped work → observed results → revised backbone.**

A small, well-understood change may stay with one agent and use an existing backbone.
Nothing requires launching helpers, assigning scores, rewriting architecture, or reopening
human decisions just because those capabilities exist.

When work is larger, the orchestrator determines which deliverables can be owned and
verified independently. The project model informs this decision but does not dictate one
agent per module. A durable module and a temporary assignment have different boundaries.
Shared decisions must be resolved before dependent work runs concurrently.

A brief contains the relevant contracts, relationships, evidence, and locators, not the
entire project narrative. Workers may find additional evidence within their assignments.
They return unexpected shared relationships to the manager, who resolves cross-slice
implications and assigns updates to the appropriate owner. The accepted project model is
then available to the next task instead of disappearing with the previous conversation.

The exact exchange uses existing [brief fields](skills/orchestrator/BRIEFS.md), with
ownership defined by the [workflow contract](skills/context-architecture/WORKFLOW.md).

## Exploration and exploitation are action values, not delivery stages

An epistemic action seeks information that can improve a decision. A pragmatic action
advances a preferred outcome. An experiment, test, or implementation can do both.

The cheap action heuristic is:

    Action value = expected progress + useful information − cost

Use coarse judgments only when a consequential next move is unclear. A question has value
when its answer can change the work, not merely because it adds knowledge. The cost includes
context, time, human interruption, and possible rework. These judgments rank permitted
moves within the current scope; they cannot buy permission to bypass a constraint.

This is distinct from the orchestrator's stages. Exploration addresses unsettled structure.
Hardening verifies a coherent arrangement being retained. A targeted investigation can
happen during hardening without reopening the entire project. If evidence invalidates a
structural assumption, only the affected scope returns to exploration through its owner.
The [coherence gate](skills/orchestrator/doctrine/stages.md) controls that transition.

## Three feedback loops with different owners

- **Model correction:** a read or experiment contradicts the expected responsibilities or
  dependencies. Context architecture helps identify the correction; the authorized owner
  updates the relevant project artifact.
- **Delivery correction:** a result invalidates an assignment boundary, resource estimate,
  or shared contract. The orchestrator revises the affected plan and integrates the change.
- **Behavior correction:** execution fails an agreed outcome. The quality process supplies
  evidence about the failure and verifies the repair.

These loops inform one another, but their evidence is not interchangeable. A good routing
prediction does not prove correct behavior. A passing test does not prove the human's
intention was understood. An orderly assignment board does not prove integration works.

## Keep optimization subordinate to correctness and human control

A small action score cannot choose weaker models behind the human's back. Capability and
effort decisions follow [model-strategy](skills/model-strategy/SKILL.md), including the
scope of the human's approval. Manager maximum-effort settings are an operating policy,
not a claim of universal benchmark superiority.

Likewise, a low estimate of wasted reading does not imply that a context window is safe.
[Context accounting](skills/orchestrator/CONTEXT.md) tracks occupancy, reserves completion
headroom, and specifies warning and recovery behavior. Unknown telemetry remains unknown;
cumulative billing and file counts are not substitutes for it.

The human supplies both evidence about a situation and decisions about desired outcomes.
An agent can inspect what the software does; it cannot infer that existing behavior must
therefore be what the human wants. Clarify consequential direction through the established
owner instead of creating a second interview inside each worker.

## Apply the same architecture to this repository

- **README:** a short entry point explaining the outcome, available skills, and how to start.
- **This document:** the optional whole-collection rationale and relationships.
- **Each SKILL.md:** a concrete responsibility, its procedure, and completion criteria.
- **Supporting documents:** conditional contracts, stage rules, runtime adapters, and techniques.
- **Reference shelves:** evidence for a specific unresolved question, not required startup reading.

Root documentation explains the collection but is not an installation dependency. A copied
skill carries its local instructions and supporting files; cooperating skills use documented
sibling contracts when available. A user need not distribute this root document to execute them.

Explanations live at the level where they change a decision. We preserve one authoritative
rule instead of copying it into every skill. Scoped excerpts in briefs are intentional views,
with locators back to their source, not independent competing policies.

## What would show that this works

Evaluate matched tasks for correct completion, missing dependencies, unnecessary reading,
rework, and the cost of maintaining the model. Include unfamiliar or cross-cutting tasks,
not just examples used to write the explanation. Better results must survive contact with
actual task evidence; fewer reads alone are insufficient.

The [predictive-processing and active-inference references](skills/context-architecture/REFERENCES.md)
motivate the proposed mechanism. They do not establish that this repository layout improves
coding agents. The action scores and context-budget defaults are operational heuristics or
policies, not constants derived from neuroscience. Installing Markdown does not change model
weights, add unavailable runtime controls, or guarantee adherence.

The intended result is a project whose accumulated structure makes future work easier to
understand and perform. Whether it does so is a question for measured use, not a benefit
we declare merely because the filing system looks like a schema.
