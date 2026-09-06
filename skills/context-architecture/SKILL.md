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
- Predictive processing and active inference motivate this engineering adaptation. Free energy is not literal context size, elapsed time, or code complexity. Action comparisons are heuristics, not a formal probabilistic calculation. Improved agent performance must be checked, not assumed.

## 1. Establish the problem

Use the agreed outcome, acceptance conditions, constraints, applicable delivery stage, and current scope from the existing plan or brief. Fill only actual gaps. Distinguish implementation facts from intended behavior; route unresolved human direction through the established decision owner in the workflow contract. Investigate implementation facts through the project; seek human domain knowledge when it is the better source for a consequential gap.

Finish when the next bounded piece of work has a clear purpose and a way to judge its result. Reuse settled context rather than repeating discovery.

## 2. Form the solution backbone

State the few relationships that explain how the solution achieves the outcome. Ask: Why is each responsibility necessary? How do the responsibilities depend on or constrain one another? Which assumptions remain uncertain? Distinguish required behavior, chosen policy, observed fact, and explanatory hypothesis where they imply different authority or checks.

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

When the next consequential action is unclear, compare a few candidates by expected progress, information that could change the work, and total cost. Include context, time, human interruption, verification, and likely rework. Prefer a cheaper, reversible action when its contribution is comparable; do not optimize one agent's lifetime by shifting unfinished work elsewhere. Use the [evaluation guide](EVALUATION.md) only when designing an experiment or when an optional coarse score would clarify a real tradeoff.

Approval, write ownership, context limits, and mandatory checks are gates, never score terms. Model-strategy owns capability and effort selection. Skip comparisons when the next step is clear; stop optional investigation when it is unlikely to change the work, without skipping required evidence or stage gates. Preserve and report unfinished work when completion is blocked.

Ask the human when their authority, experience, or reframing can resolve a consequential gap better than more inspection. Frame a concrete tension around the governing purpose or principle, not just an implementation vote. Use the existing human-decision skill or channel; workers route shared questions through the manager. A preference establishes direction, a factual assertion supplies evidence, and an architectural implication remains an inference to test.

## 5. Add detail through scoped work

Honor applicable project routing instructions. Before an uncertain read, state the gap it serves; make any useful expectation explicit and revisable. Research hypotheses are optional, not conclusions to reproduce. Reuse an established route; fetch exact facts directly when no broader understanding is needed. A direct search or symbol lookup may be cheaper than descending from the root.

Read enough to resolve the gap, including necessary cross-branch contracts, within the assigned scope. Use bounded experiments for uncertain arrangements; apply the established quality policy to retained implementation. Fundamentals-first does not waive checks or require tests before every exploratory read. Fundamentals-first means establishing enough structure for the next detail, not completing an exhaustive design before any code is written.

Example: if progress disappears after reload, distinguish “not saved” from “not restored.” Inspecting persisted state can separate these explanations more cheaply than reading the entire application. Let the observation determine the next branch.

## 6. Correct the model as the project teaches you

Compare important expectations with observations. Label unresolved claims as tentative, supported, or contradicted; use numbers only if they improve a real decision. When observations fit none of the candidate explanations, revise the candidates rather than forcing a match.

When a mismatch appears, distinguish an implementation defect, an inaccurate explanation of existing code, and unresolved or changed intent. Fix code against the agreed requirements, revise an inaccurate backbone, or return the intent decision to the human. Neither documentation nor implementation alone proves that the user's problem is solved.

Tools and procedures are project context too. For a capability gap or obsolete tool, use the local [tool lifecycle](../turn-to-life/TOOLS.md) when available; otherwise apply the same scoped construction and verification principles. Judge sufficiency across current acceptance and credible future changes, including lifecycle cost. A replaceable boundary may earn its place without a plugin framework; keep authored tools repo-local.

Update the working map within write ownership. Persist conclusions and evidence in existing project artifacts, not another competing glossary or plan. Workers report shared relationship changes with locators; the manager adjudicates them, assigns updates to their owner, and verifies affected contracts. Preserve completed work. Keep references aligned with moves and consolidate the accepted model at integration.

## 7. Verify that the architecture earns its cost

Check solution logic, implementation, and process economy separately where affected. For substantial structural changes, use the [evaluation guide](EVALUATION.md): include an unfamiliar or cross-cutting task not used to write the explanation, verify the outcome, and compare resource use at the same quality bar. An abstraction should preserve a necessary distinction; a short explanation or implementation alone does not establish elegance.

Supply relevant evidence through existing acceptance/report fields, not a second testing process. Routing checks supplement behavior, integration, and project-required checks. Distinguish peak context, total processing, and elapsed time; occupancy and recovery remain governed by the orchestrator or applicable local policy. Include failed attempts, handoffs, rework, and model maintenance. Retain useful structure and simplify overhead within scope; report material revisions and uncertainty, not a bookkeeping transcript.

## Sources on demand

Read [REFERENCES.md](REFERENCES.md) only to investigate the theoretical basis or limits of this adaptation.
