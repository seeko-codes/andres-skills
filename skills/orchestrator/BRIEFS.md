# Locally complete dispatch briefs

Every brief contains the following compact fields. Supply the information needed to
execute; do not paste the entire manager conversation. Read [core.md](doctrine/core.md)
and only the matching task guidance when preparing the brief.

| Field | Contents |
|---|---|
| DELIVERABLE | Exact output and its necessary contribution to the horizontal goal |
| STAGE | Exploration or hardening, why, and evidence needed to exit the stage |
| CONTRACT | Experiment/question in exploration; settled requirements/interfaces in hardening; constraints in both |
| COMPONENT | For implementation: public contract, required/provided dependencies, owned state, wiring owner, and replacement constraints |
| INPUTS | Curated sources with read scope and purpose; relevant dependency outputs |
| AUTHORITY | Local choices the agent owns; cross-slice decisions it must escalate |
| BOUNDS | Exact write-set, isolation path, applicable local instructions; no delegation |
| ACCEPTANCE | Checks and evidence needed to accept the result |
| RESOURCES | Actual model/effort, context ceiling, warning level, monitoring availability |
| REPORT | Output locations, check results, consequential rationale, deviations and gaps |

Work-alone instruction: Do the assigned work directly. Do not spawn agents or launch
another agent CLI. Ask the manager to re-slice when the contract cannot be fulfilled
within its boundaries. The manager checks context sizing using measured occupancy or the explicit estimated/unknown
fallback in CONTEXT.md; it does not depend on this request.

Research assignments name the question, how its answer affects the plan, and evidence
needed; hypotheses are optional and must not bias findings. Exploration assignments commission bounded experiments; hardening assignments establish
shared requirements while preserving local implementation autonomy. Review assignments
name the target, relevant requirements, risk, and requested independent verdict.

Acceptance instruments must suit the task and stage. Read [stages.md](doctrine/stages.md)
for the coherence gate and prototype-to-hardening transition. Do not impose fake failing
checks on investigations, document edits, or already-working prototype characterization.
