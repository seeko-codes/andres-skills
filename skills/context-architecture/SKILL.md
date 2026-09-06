---
name: context-architecture
description: Builds repositories fundamentals-first so agents can reach and understand relevant code with little wasted context. Use when scaffolding projects, adding responsibilities or features, revising module boundaries, or repairing costly repository navigation.
---

# Context Architecture

Build the repository as a revisable schema: **problem → solution logic → concepts → details**. Each addition should leave useful software and a clearer route to understanding it. Minimize unnecessary context subject to solving the user's problem correctly; a tidy repository is a means, not the goal.

## Scope and boundaries

- Static context is project material available through files: source code, Markdown, tests, configuration, and other artifacts. Dynamic context is supplied during the current conversation. Static does not mean immutable or automatically loaded.
- Apply this method while constructing code, not merely by documenting finished code. For existing projects, preserve working behavior and revise only the affected structure unless broader restructuring is justified and authorized.
- This skill owns reusable project structure, not delivery control. The orchestrator owns scope, stages, delegation, budgets, and integration; its dependencies retain their authority. Apply the [workflow contract](WORKFLOW.md) when connecting these responsibilities. A worker uses its assigned contract and does not restart orchestration.
- Predictive processing and active inference motivate this engineering adaptation. The scores below are heuristics, not measured probabilities or a formal free-energy calculation. Improved agent performance must be checked, not assumed.

## 1. Establish the problem

Use the agreed outcome, acceptance conditions, constraints, stage, and current scope from the existing plan or brief. Fill only actual gaps. Distinguish implementation facts from intended behavior; route unresolved human direction through the established decision owner in the workflow contract. Investigate implementation facts through the project.

Finish when the next bounded piece of work has a clear purpose and a way to judge its result. Reuse settled context rather than repeating discovery.

## 2. Form the solution backbone

State the few relationships that explain how the solution achieves the outcome. Ask: Why is each responsibility necessary? How do the responsibilities depend on or constrain one another? Which assumptions remain uncertain?

Use conditional explanations, not topic lists. “Selection consumes current learner evidence, which evaluation updates” provides more routing information than “selection, evaluation, progress.” These are working hypotheses, not immutable first principles.

The backbone must support three useful predictions for a task:
- **Target:** which responsibility should contain the answer, and why.
- **Support:** which contracts or neighboring relationships are needed to understand it.
- **Exclusion:** which implementation details should remain irrelevant unless evidence contradicts that expectation.

Finish when these expectations distinguish plausible routes. If the explanation fits every possible arrangement, sharpen it before treating it as routing logic. It need not predict exact filenames, constants, or algorithms.

## 3. Express the backbone in code structure

Derive concrete responsibilities and their interfaces. Use cohesion, likely changes, and the knowledge callers actually need to judge boundaries. A processing sequence can explain behavior without being the correct module decomposition.

- Give code a meaningful home and names that expose its responsibility. Make expected targets reachable through names, symbols, or concise references to actual locations.
- Keep related implementation decisions together; expose necessary contracts rather than forcing callers to learn internals.
- Make real dependency direction explicit. Preserve necessary cross-branch relationships instead of forcing every relationship into a single-parent tree.
- Treat logic, concepts, and details as levels of understanding, not required directory names. Use the shallowest structure that clearly distinguishes responsibilities; deepen or collapse it when actual navigation warrants it.
- Add summaries only when they supply non-obvious purpose, relationships, constraints, or routes. Keep broad summaries free of local implementation detail. Point to authoritative facts rather than duplicating them.

Finish when a relevant responsibility can be located and interpreted without opening unrelated implementations. Do not manufacture folders, abstractions, or documents just to complete this sequence.

## 4. Choose whether to inspect, ask, experiment, or implement

Use the current model to anticipate what an action will reveal or accomplish. Epistemic actions improve task-relevant understanding; pragmatic actions advance the solution. An action can do both in either delivery stage. These values do not replace the orchestrator's exploration/coherence/hardening gates. Reorganizing without discriminating evidence is not automatically useful exploration.

When the next consequential action is unclear, compare a few candidates using:

    Action value = expected progress + useful information − cost

Score each term coarsely as 0, 1, or 2:
- **Progress:** none / advances a necessary part / directly advances an acceptance condition.
- **Useful information:** none / refines the current explanation / distinguishes explanations that imply different next actions.
- **Cost:** small / moderate / large, considering context, time, human interruption, and likely rework.

These are rough comparisons within the current contract, not calibrated quantities. Approval, write ownership, context limits, and mandatory checks are gates, never score terms. Model-strategy owns capability and effort selection. Break close ties with the cheaper, more reversible action. Skip scoring when the next step is clear; stop optional investigation when it is unlikely to change that next step, without skipping required evidence or stage gates.

The human supplies both evidence and direction. Preserve their authority over desired outcomes and consequential tradeoffs. Workers route unresolved intent and shared decisions through the manager; do not start a competing human interview.

## 5. Add detail through scoped work

Honor applicable project routing instructions. Before an uncertain read, state the gap it serves; make any useful expectation explicit and revisable. Research hypotheses are optional, not conclusions to reproduce. Reuse an established route; fetch exact facts directly when no broader understanding is needed. A direct search or symbol lookup may be cheaper than descending from the root.

Read enough to resolve the gap, including necessary cross-branch contracts, within the assigned scope. Use bounded experiments for uncertain arrangements; apply the established quality policy to retained implementation. Fundamentals-first does not waive checks or require tests before every exploratory read. Fundamentals-first means establishing enough structure for the next detail, not completing an exhaustive design before any code is written.

Example: if progress disappears after reload, distinguish “not saved” from “not restored.” Inspecting persisted state can separate these explanations more cheaply than reading the entire application. Let the observation determine the next branch.

## 6. Correct the model as the project teaches you

Compare important expectations with observations. Label unresolved claims as tentative, supported, or contradicted; use numbers only if they improve a real decision.

When a mismatch appears, distinguish an implementation defect, an inaccurate explanation of existing code, and unresolved or changed intent. Fix code against the agreed requirements, revise an inaccurate backbone, or return the intent decision to the human. Neither documentation nor implementation alone proves that the user's problem is solved.

Update the working map within write ownership. Persist conclusions and evidence in existing project artifacts, not another competing glossary or plan. Workers report shared relationship changes with locators; the manager adjudicates them, assigns updates to their owner, and verifies affected contracts. Preserve completed work. Keep references aligned with moves and consolidate the accepted model at integration.

## 7. Verify that the architecture earns its cost

Use actual tasks to check that the backbone identifies the target, necessary supporting context, and defensible exclusions. For substantial structural changes, include an unfamiliar or cross-cutting task not used to write the routing explanation. Verify the task outcome; plausible routing is not sufficient evidence.

At meaningful checkpoints, estimate:

    Context waste ≈ unnecessary material read / total material read

Include orientation, summaries, and detours. Rough read counts ignore size differences; use size estimates when those differences matter. Judge necessity against verified task evidence. This routing-cost proxy is not live context occupancy; budget accounting and recovery remain governed by orchestrator/CONTEXT.md.

Compare similar tasks and include model-maintenance cost. Reduced reading with missed dependencies is failure. Supply routing-check evidence through existing acceptance/report fields; it supplements, never replaces, behavior, integration, or project-required checks. Retain useful structure and simplify overhead within scope. Report material revisions and uncertainty, not a bookkeeping transcript.

## Sources on demand

Read [REFERENCES.md](REFERENCES.md) only to investigate the theoretical basis or limits of this adaptation.
