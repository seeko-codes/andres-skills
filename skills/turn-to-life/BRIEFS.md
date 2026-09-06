# Locally complete dispatch briefs

Every brief contains the following compact fields. Supply the information needed to
execute; do not paste the entire manager conversation. Read [core.md](doctrine/core.md)
and only the matching task guidance when preparing the brief.

| Field | Contents |
|---|---|
| DELIVERABLE | Exact output and its necessary contribution to the horizontal goal |
| STAGE | For delivery work: exploration or hardening, why, and exit evidence. For standalone research/review: task type and completion evidence; no invented implementation stage |
| CONTRACT | Experiment/question in exploration; settled requirements/interfaces in hardening; question or review target for standalone inquiry; constraints in all cases |
| INPUTS | Required sources with read scope and purpose; relevant backbone relationships/contracts and dependency outputs; optional lookup locators labeled with the question that would trigger retrieval. Distinguish tentative explanations from requirements |
| AUTHORITY | Local choices the agent owns; cross-slice decisions it must escalate; any scoped push/PR/release authority, otherwise local work only |
| BOUNDS | Exact write-set, isolation path, applicable local instructions; for Git writes, branch/base commit and index ownership under [GIT.md](GIT.md); no delegation |
| ACCEPTANCE | Checks and evidence needed to accept the result |
| RESOURCES | Actual model/effort, human effort choice or covering policy and its scope, context ceiling, warning level, monitoring availability; resolved optimization priorities and remaining shared optional-refinement allowance when applicable |
| REPORT | Output locations, check results, consequential rationale, deviations and gaps; observed shared-relationship mismatches with evidence and proposed owner updates when relevant |

Work-alone instruction: Do the assigned work directly. Do not spawn agents or launch
another agent CLI. Ask the manager to re-slice when the contract cannot be fulfilled
within its boundaries. The manager checks context sizing using measured occupancy or the explicit estimated/unknown
fallback in CONTEXT.md; it does not depend on this request.

Research assignments name the question, how its answer affects the plan, and evidence
needed; hypotheses are optional and must not bias findings. Exploration assignments commission bounded experiments; hardening assignments establish
shared requirements while preserving local implementation autonomy. Review assignments
name the target, relevant requirements, risk, and requested independent verdict.

For structural changes, include relevant routing checks in ACCEPTANCE alongside functional
checks. The manager adjudicates shared-model revisions and assigns their update to the owner;
workers preserve write boundaries. Supply the relevant backbone, not the entire architecture
skill or its theory shelf, when a worker only needs an established local contract.

Acceptance instruments must suit the task and stage. Read [stages.md](doctrine/stages.md)
for the coherence gate and prototype-to-hardening transition. Do not impose fake failing
checks on investigations, document edits, or already-working prototype characterization.
