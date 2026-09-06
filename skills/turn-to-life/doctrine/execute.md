# Autonomous implementation by stage

The brief states EXPLORATION or HARDENING. Read [stages.md](stages.md) when choosing or
transitioning stages. If unspecified, infer from whether a consequential structural question
remains and state the choice. Own local decisions; escalate changes affecting other slices.

In exploration, the contract defines the experiment, question, boundaries, and evidence to
return. Architecture may be provisional. Do not automatically load lean-quality. Use targeted
checks and prototypes to compare arrangements; report findings and deferred quality work.

In hardening, requirements, shared interfaces and acceptance are established. Apply lean-quality
when available. If absent, use proportionate behavior checks, bug reproductions, relevant
static/build checks, and integration or smoke checks for changed seams. Use screenshots and
real interactions for UI where relevant. Do not claim post-hoc prototype tests were test-first.

Stay within write ownership and verified isolation. Respect project rules and higher-priority
user/runtime instructions in both stages. Follow [GIT.md](../GIT.md) before repository edits
or Git operations: preserve an owned, reviewable commit or report the named artifact and why
committing is unavailable/prohibited. Preserve unrelated dirty/staged work. Mark exploratory
checkpoints as prototypes, not completed production deliverables.
Return stage, outputs, checks, consequential choices, deviations, and unresolved work. Retained
prototype code must pass hardening before being reported as production-ready.
