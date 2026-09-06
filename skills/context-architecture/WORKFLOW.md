# Workflow contract: reusable structure and scoped execution

## Shared outcome and distinct responsibilities

Build software that satisfies the human's problem while reducing unnecessary context for later work. Context architecture preserves a reusable problem-solving backbone; orchestration turns the relevant part into a bounded, verifiable assignment. Neither purpose replaces the other. Keep the skills separate because the project model persists across tasks while assignments, owners, and execution stages change. Connect them through scoped evidence rather than duplicate either procedure.

| Concern | Owner | Context architecture contributes |
|---|---|---|
| Project purpose, approved scope, priorities, consequential tradeoffs | Human; [grill-with-docs](../grill-with-docs/SKILL.md) facilitates | Identifies missing decisions and their structural consequences; reuses recorded answers |
| Reusable problem/logic/concept/detail relationships | [Context architecture](SKILL.md) | Meaningful responsibilities, contracts, locators, uncertainty, and routing checks |
| Stage, assignment boundaries, ownership, delegation, integration | [Orchestrator](../orchestrator/SKILL.md) | Relevant backbone and dependency evidence, not a second execution plan |
| Context ceilings, occupancy, and recovery | [Orchestrator context rules](../orchestrator/CONTEXT.md) | Estimates avoidable reading and maintenance cost, not occupancy telemetry |
| Model capability and effort | [Model-strategy](../model-strategy/SKILL.md) recommends; the human approves effort | Explains remaining uncertainty and verifier strength; its action score does not select resources |
| Verification of retained implementation | [Lean-quality](../lean-quality/SKILL.md) | Adds routing and structural acceptance checks alongside behavior/integration checks |
| Explicit test-driven-development method | [TDD](../tdd/SKILL.md) | Supplies behavioral contracts, not tests coupled to the chosen folder layout |

Owner links resolve decisions; they are not a command to load every skill. Respect higher-priority instructions and explicit user direction. The dedicated TDD skill is reached when requested; this does not remove red-green-refactor already specified by the applicable hardening policy.

The root collection rationale is explanatory, not a runtime dependency. When a skill is
installed alone, retain its local project-policy fallback; optional companion links do
not require installing or loading the whole collection.

## Exchange existing artifacts, not whole histories

Use the project's existing plan, architecture notes, glossary, and contracts. Keep each fact authoritative in one place; scoped excerpts may carry necessary context into a brief with a source locator. Do not place implementation-routing detail in a glossary reserved for domain meaning.

1. The orchestrator supplies the agreed goal, stage, acceptance, boundaries, and current decisions. With no orchestrator present, work locally using applicable project policy; do not create a delegation process merely to use this skill.
2. Context architecture supplies the relevant backbone: responsibilities, contracts, dependency directions, actual locators, and consequential unresolved assumptions. Keep the whole project purpose visible without loading every branch.
3. The orchestrator uses that evidence to make assignments. A durable module is not automatically one temporary work slice, and a folder is never an automatic agent allocation. Resolve shared decisions before dependent concurrent work.
4. Workers retrieve and reason within their contracts. Local implementation choices remain theirs. Unexpected shared dependencies, changed scope, or ownership conflicts go to the manager with evidence; they do not authorize broader edits, more workers, or a second human interview.
5. The manager verifies results and cross-slice implications, assigns shared-model updates to their owner, and integrates accepted changes before relying on the revised model for dependent work.

Use existing [brief fields](../orchestrator/BRIEFS.md): CONTRACT for relevant established interfaces and constraints; INPUTS for scoped backbone sources and optional locators; AUTHORITY/BOUNDS for decision and write ownership; ACCEPTANCE for routing checks where relevant; REPORT for observed mismatches, model revisions, and verification. Tentative explanatory hypotheses must remain distinguishable from binding requirements.

## Stage compatibility

An epistemic action gains useful evidence; a pragmatic action advances preferred outcomes. These are action values, not delivery stages. A prototype can do both; a targeted investigation can happen during hardening without reopening the entire project.

Follow the orchestrator's [coherence gate](../orchestrator/doctrine/stages.md). Prediction agreement alone does not establish coherence or correctness. When evidence invalidates a structural assumption, return only the affected scope to exploration through its owner. Preserve valid implementation and settled requirements.

The cheap action score chooses among permitted next moves within current scope, resources, and stage. It cannot skip mandatory checks, reinterpret a context breach as worth the cost, change effort, expand write ownership, or declare a prototype production-ready.

## Compatibility checks

- **Small known change:** stay local; reuse the backbone and fetch the relevant contract. No mandatory scoring, agent launch, or architecture rewrite.
- **Uncertain arrangement:** name the question and stopping evidence, then run a bounded experiment. An attractive explanation or passing prototype does not satisfy the hardening gate.
- **Shared-interface discovery:** a worker reports the mismatch and proposed implications; the manager resolves ownership and dependent contracts before integration.
- **Human ambiguity:** unresolved intended behavior goes through the established decision channel. Existing code is evidence of what happens, not authority over what should happen.
- **Budget pressure:** a high-value action still obeys occupancy warnings and recovery. Routing-cost estimates do not replace measured/estimated/unknown budget reporting.
- **Retained behavior:** architecture predictions inform where to inspect; the existing quality contract determines what must be verified. Documentation-only edits require appropriate document checks, not invented behavioral tests.

These are review cases, not evidence of measured runtime improvement. Evaluate concrete runs before claiming the combination makes agents more effective.
