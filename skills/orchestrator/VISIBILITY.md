# One human-readable view

At every level explain the action, purpose, current evidence, and next decision. The
Wayfinder shows the long-range sequence and handoffs; the orchestrator shows goals,
batches and assignments; workers provide meaningful progress through their manager.
Centralize this into one coherent view instead of flooding the human with parallel transcripts.

At launch and significant changes, show:

| Agent / parent | Deliverable and why | Model / effort | Depends on | Context / limit | Status |
|---|---|---|---|---|---|

Use real run identifiers once launched; planned agents are labeled planned. Context values
include measured/estimated/unknown and freshness. Show the active batch and queued work.
Status vocabulary: planned, running, blocked, verifying, integrating, complete, handed off.

Explain planning, dispatch, blockers, changed decisions, verification, integration, and handoff.
During long work provide a concise heartbeat, normally within 60 seconds when the runtime
permits, without claiming progress that did not occur. Include what is being resolved next.
Do not issue updates for every tool call or repeat the entire board without a meaningful change.

Escalations to the human state the decision, why evidence cannot settle it, alternatives,
consequences, and recommendation. Highest-level direction and consequential uncertain
tradeoffs belong to the human. Routine execution, telemetry checks, and authorized handoffs do not.
Summaries give decision rationale and evidence, never hidden chain-of-thought transcripts.
