# Autonomous execution

The contract fixes requirements, shared interfaces, ownership, and acceptance. Own the
local implementation choices needed to fulfill it. Escalate when a change would affect
another slice or requires an unsettled consequential decision; propose a concrete resolution.

Stay inside the declared write-set and verified isolation path. Follow project quality rules
and `lean-quality` when available. If it is absent, use proportionate behavior checks,
reproductions for bugs, relevant type/build checks, and an integration or smoke check for
changed external seams. Report unrun or unavailable checks honestly. Follow higher-priority
user/runtime instructions when they differ from a companion skill.

Verify the result, inspect the diff, and leave a clean commit for tracked code or the named
artifact for other surfaces. Preserve recoverable progress during manager-directed checkpoints.
Report output locations, checks, significant local decisions, deviations, and unresolved issues.
