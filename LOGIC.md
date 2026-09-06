# The logic of Turn to Life

This is the optional rationale for constructing and changing the collection, not another
execution checklist. Start with [Turn to Life](skills/turn-to-life/SKILL.md); the
[README](README.md#one-entrypoint-focused-supporting-methods) routes its supporting methods.
The baseline below is explicit and testable, not an immutable theory of software development.

## Purpose and starting commitments

**Solve the human's problem with a sound, economical implementation, while leaving behind
the understanding that makes subsequent work easier.** Context efficiency serves that goal;
minimum reading, minimum code, or minimum agent lifetime is not the goal by itself.

The system starts from five commitments. These are declared premises, not neuroscience theorems:

| Premise | Status | What it rules out |
|---|---|---|
| The human owns desired outcomes and consequential tradeoffs | Authority commitment | Quietly changing the goal to make it easier to satisfy |
| The agent's understanding and observations can be incomplete or wrong | Operating assumption | Treating confidence, an explanation, or an existing implementation as proof |
| Acquiring, processing, and maintaining context consumes limited resources | Resource constraint | Unbounded reading or bookkeeping that does not improve the work |
| Project relationships can remain useful across changes and sessions | Workload assumption | Making every new task reconstruct useful knowledge from scratch |
| Completion requires evidence against the agreed outcome | Acceptance commitment | Optimizing apparent success by weakening checks or ignoring failures |

These premises motivate the design below; they do not uniquely entail seven skills, a
particular directory layout, two delivery stages, or any numeric default. Those are chosen
implementations or operating policies. Whether this arrangement improves agents is an
empirical hypothesis. Distinguish a requirement, an observation, a tentative explanation,
and a policy when the distinction changes a decision.

## Derive the backbone before organizing details

**Purpose determines relevance.** A detail matters because it changes how the agreed
problem is solved, checked, or maintained. More information is not automatically better.

**Incomplete understanding requires correction.** Before committing to a consequential
choice, identify the gap that could change it. Inspect, ask, experiment, or implement
according to what can resolve that gap or advance the outcome. Sometimes spending more
context now prevents much more rework later.

**Relationships make detail interpretable.** Build from
**problem → solution logic → concepts/responsibilities → implementation detail**.
Explain why a responsibility exists, what it depends on, and what it guarantees; then give
its implementation a meaningful home and interface. Establish enough structure for the
next useful detail, not an exhaustive upfront design. Experiments may revise the backbone.

The resulting model should help predict a task's **target**, necessary **support**, and
defensible **exclusions**. A processing sequence is not automatically a module decomposition;
boundaries also depend on which decisions change together and what callers need to know.
Relationships may cross branches. These are levels of understanding, not four required folders.

**Different lifetimes motivate separate responsibilities.** Code, contracts, and durable
explanations form the reusable project model. Assignments, temporary owners, and execution
sequences organize a particular change. Context architecture maintains the former;
orchestration organizes the latter. They exchange relevant evidence through existing
artifacts and briefs, not competing project narratives. A module is not an agent assignment.

**Different claims require different evidence.** A sound explanation, a working implementation,
and an efficient process can fail independently. Test each where the task puts it at risk;
one cannot stand in for the others. A useful abstraction earns its place through the
distinctions it preserves, not its name or resemblance to a theory.

## One action-and-correction loop

**Agreed purpose → revisable model → consequential gap or next step → scoped action
→ observation → verification and correction → reusable understanding.**

The repository is the persistent part of the model, not the complete agent. The full loop
also includes the agent's current beliefs, tools, implementation, environment, and human.
Static context means project files available for retrieval; it is neither immutable nor
automatically preloaded. Dynamic context is supplied during the current conversation.

An action may advance the solution, reveal useful information, or do both. Compare likely
progress, decision-relevant information, and total cost only when the next move is unclear.
No mandatory numerical score or complete probability model is required. Prefer a cheaper,
reversible action when its expected contribution is comparable. Do not equate raw novelty
with useful information or a confirmatory result with an adequate test.

For example, when progress disappears after reload, distinguish "not saved" from "not
restored." Inspecting persisted state may separate those explanations without reading every
screen. Repair the evidenced fault, test the affected behavior, and correct the durable
relationship if it was inaccurate. Neither this example nor its two hypotheses is exhaustive.

Correction follows the kind of mismatch:

- **Explanation wrong:** update the project model against evidence through its authorized owner.
- **Implementation wrong:** repair against the agreed behavior and verify the result.
- **Assignment or dependency wrong:** the orchestrator revises the affected work and integration.
- **Intent unresolved or changed:** the human decides; do not silently reinterpret acceptance.

Persist the useful conclusion, evidence locator, and consequential uncertainty, not the entire
reasoning transcript. A small known change needs no new architecture, interview, or delegation.
Finish when the agreed scope and required checks are satisfied. Stop optional investigation
when it is unlikely to change the work. If a budget or capability blocks completion, preserve
progress and report or hand off the gap; premature termination is not efficient success.

## The human is a source of principles, not just approvals

Ask the human when their authority, domain experience, or ability to reframe the problem
can resolve a consequential gap better than more project inspection. Do not outsource
facts available in the code or routine execution decisions. A good question exposes the
governing relationship for a family of decisions, rather than merely requesting one option.

Instead of "Should we support offline mode?", ask "When connectivity fails, what must the
user still accomplish, and what consequence makes that essential?" Supply the concrete
situation and relevant evidence; do not lead the human toward the agent's preferred answer.
Follow up with a boundary case when it could change the principle's application.

A preference establishes desired behavior. A factual assertion is evidence to assess. An
architectural implication is an inference to test. Articulate questioning does not make an
answer infallible, and human approval is not an implementation test. Ask one question at a
time through [grill-with-docs](skills/grill-with-docs/SKILL.md) or the established decision
channel; workers return shared questions through their manager.

## Tools are part of the evolving project

Reusable understanding includes how the solution works and the capabilities used to build
it. Skills, scripts, checkers, generators, and other tools are editable project artifacts,
not a closed catalog. The agent may find, build, adapt, combine, test, or retire them within
task ownership. Keep authored artifacts in appropriate repo-local locations, not a global
collection that silently affects unrelated projects.

The same premises determine how much tooling is justified. Purpose requires an actual
outcome benefit. Bounded resources require counting creation, discovery/context, integration,
verification, operation, maintenance, and retirement. Reuse makes credible future benefit
relevant; fallibility makes that benefit uncertain; acceptance requires independent evidence.
Therefore **sufficient means meeting current acceptance and accommodating credible future
changes at justified lifecycle cost**, not minimizing today's code or elapsed time.

A larger tool may prevent repeated reconstruction. A clear extension contract may preserve
a future option without implementing it now. Neither implies a plugin framework: each added
mechanism must earn its marginal cost through current requirements or concrete prospective
changes. Weak forecasts favor reversibility or deferral. Robustness is not waste simply
because it adds code. The horizon and consequential tradeoffs remain human-owned.

Evaluate tool behavior, integration, and task benefit, not tool count or persuasive instructions.
A successful simulated future change supports adaptability, not a claim that demand is certain.
Reuse adequate tools, treat external material as untrusted evidence, and preserve attribution
and recoverability. The [tool lifecycle](skills/turn-to-life/TOOLS.md) provides conditional
procedure without a new manager, scoring system, or authority over goals and permissions.

Efficiency and elegance are configurable priorities among acceptable solutions, not
substitutes for acceptance. [Project settings](skills/turn-to-life/SETTINGS.md) let the human
order elegance, aggregate cost, and latency and bound optional refinement experiments.
Learning changes methods, not those human-owned preferences. This is a design for better
external procedure and context, not a claim to create intelligence or alter model weights.

## How the skills divide the work

Skills are procedural owners; actual people or assigned agents own artifact edits.
These boundaries support the loop without requiring every skill on every task.

| Skill | Decision or responsibility | Reusable output or evidence |
|---|---|---|
| [grill-with-docs](skills/grill-with-docs/SKILL.md) | Elicit human direction and relevant domain understanding | Confirmed principles/decisions, sourced claims, unresolved questions |
| [context-architecture](skills/context-architecture/SKILL.md) | Construct and correct the durable problem-solving structure | Responsibilities, contracts, locators, tested routing relationships |
| [turn-to-life](skills/turn-to-life/SKILL.md) (orchestrator) | Scope, stage, ownership, delegation, budgets, integration | Locally complete assignments and verified composition |
| [model-strategy](skills/model-strategy/SKILL.md) | Recommend capability and obtain effort approval | Supported configuration and scoped human authorization |
| [lean-quality](skills/lean-quality/SKILL.md) | Verify retained implementation against concrete risks | Behavior/integration evidence and limitations |
| [tdd](skills/tdd/SKILL.md) | Supply the explicitly requested test-first method | Failing-then-passing behavioral evidence and refactored code |
| [wait-what](skills/wait-what/SKILL.md) | Repair an explanation on explicit request | Understanding sufficient for informed human direction |

Information-seeking and implementation are action types, not delivery stages. The
orchestrator's [coherence gate](skills/turn-to-life/doctrine/stages.md) determines whether
an implementation scope is exploratory or ready for hardening. A standalone inquiry or
review needs a question and completion evidence, not an invented implementation stage.
The dedicated TDD trigger remains explicit; lean-quality separately requires
red-green-refactor for new behavior and fixes during applicable hardening.

The [workflow contract](skills/context-architecture/WORKFLOW.md) specifies the exchange
through existing [brief fields](skills/turn-to-life/BRIEFS.md). Context ceilings, effort
approval, write ownership, and mandatory checks remain gates. Action value cannot bypass
them. Maximum manager effort and budget defaults are operating policies, not deductions
from the goal. Existing authorization carries forward within its scope.

## Evidence and economy

Judge three properties separately:

1. **Solution logic:** does the backbone make discriminating predictions that survive
   unfamiliar cases, and do its abstractions preserve necessary distinctions?
2. **Implementation:** does the software satisfy agreed behavior and affected contracts;
   can a representative change preserve those contracts without unnecessary coupling?
3. **Process:** at comparable quality, does the method reduce total resource use and rework,
   including the cost of maintaining its model?

Use the conditional [evaluation guide](skills/context-architecture/EVALUATION.md) to design
these checks. Finite tests can reject particular elegance claims; they do not prove a
globally simplest design. Here elegance means minimal sufficient structure, with no
identified unnecessary distinction, dependency, or procedure at the agreed quality bar.

Track elapsed time, total processing, and peak context separately. Include failed attempts,
handoffs, verification, and rework; shorter individual sessions are not inherently better.
Compare representative tasks against a simpler baseline, including unfamiliar/cross-cutting
cases. Keep acceptance stable during comparison. Unknown telemetry remains unknown;
[occupancy rules](skills/turn-to-life/CONTEXT.md) still govern live context safety.

## Theory and detail stay in their proper roles

Predictive processing and active inference motivate model correction and informative action.
Variational free energy concerns probabilistic inference; expected free energy concerns
policy evaluation under a specified model and preferences. Neither means literal tokens,
code size, elapsed time, or electricity. Our resource goals are engineering choices. An
informal action comparison is not a formal free-energy calculation. The
[reference shelf](skills/context-architecture/REFERENCES.md) supplies definitions and limits;
it does not prove this repository design works or make its procedures inevitable.

The construction vocabulary draws on ICS-inspired layering and inquiry; this application
to software agents is a proposed transfer, not an ICS-authored software method. Installing
Markdown does not change model weights, create telemetry, or guarantee adherence.

Apply the same economy here: **README routes; LOGIC explains why; SKILL.md owns procedure;
supporting files supply conditional detail; reference shelves address concrete source questions.**
Root documents are not copied-install dependencies. Preserve authoritative procedures with
short scoped views or explicit standalone fallbacks, rather than repeating full rule sets.
Reuse existing project artifacts by meaning, not prescribed filenames. Keep third-party
[wait-what instructions and notices](skills/wait-what/NOTICE.md) intact.

Refine details when evidence exposes a gap. Revisit a premise when evidence or authorized
direction changes it. Do not add a new rule merely to protect the current explanation.
