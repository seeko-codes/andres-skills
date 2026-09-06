# Context allocation and measurement

The manager curates context to make each agent deeply informed about its own contract.
Start with the smallest sufficient corpus: local routing instructions, exact interfaces,
relevant source and evidence, dependency outputs, and acceptance criteria. Include only
global facts that change how this deliverable must be fulfilled. Shared constraints may
appear in multiple briefs. Narrow responsibility does not mean micromanaging local choices.

Allow targeted retrieval within the contract when evidence is missing. Do not tour the
whole repository or inherit full conversation history merely for convenience. Escalate
when retrieval reveals a changed scope, shared decision, or dependency. A researcher may
need broad sources for a narrow question; relevance, not directory size alone, determines its corpus.

Routing-cost or context-waste estimates from context architecture evaluate unnecessary
reading and model maintenance. They are not occupancy telemetry, do not change these
limits, and cannot authorize more context growth after a breach.

## Budget accounting

`max_context_per_agent` defaults to 100000 tokens and is user-configurable. Apply it to
workers, orchestrators, and the optional Wayfinder. `context_warning_fraction` defaults
to 0.8 and is also user-configurable. Require a positive token limit and a fraction strictly
between zero and one; explain invalid settings rather than silently using them.

Budget instructions + initial inputs + retrieved/tool content + working history + room
for completion and verification. Leave headroom at dispatch. Use live context-occupancy
telemetry, not cumulative billing tokens across calls, as the measurement. Report source
and timestamp. Do not conflate context windows with lifetime token usage.

Check on native progress events and before additional large reads or dispatches. Crossing
the warning level triggers a checkpoint and remaining-work review. Exceeding the ceiling
is a sizing failure even if the worker says it is fine. Do not wait for self-report.
Preserve evidence of the peak; compaction does not erase the sizing failure.

If occupancy is unavailable, label it unknown or estimated, state the estimation method,
and use conservative assignments and checkpoints. Never invent live telemetry or promise
an enforced limit without monitoring support. If the user requires strict enforcement and
no measurement/control exists, report that specific capability gap.

## Recovery and continuity

At a warning, checkpoint outputs, decisions, checks, and remaining work. At a breach,
stop further context growth using supported controls; preserve recoverable edits before
termination. Resume only a narrowed remainder in fresh context or re-slice it. Record
which input or work expansion caused the oversized assignment to improve the next cut.
No destructive reset or deletion of unfinished work is implied.

A handoff contains: goal and acceptance; configuration and user-approved effort policy/choices with their scope; completed outputs and exact
commits/artifact locations; relevant rationale; unresolved decisions; next assignments;
active run IDs, worktree paths, ownership, and unmerged changes. Quiesce active workers
or explicitly transfer their handles if supported. Never duplicate dispatch because a
successor cannot see a predecessor's runs. With Wayfinder enabled it coordinates renewal;
otherwise use available native handoff controls and identify any unavoidable human step.
