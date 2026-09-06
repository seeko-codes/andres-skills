# One human-readable view

At every level explain the action, purpose, current evidence, and next decision. The
Wayfinder shows the long-range sequence and handoffs; the orchestrator shows goals,
batches and assignments; workers provide meaningful progress through their manager.
Centralize this into one coherent view instead of flooding the human with parallel transcripts.

At launch and significant changes, show:

| Agent / parent | Deliverable and why | Model / effort | Depends on | Context / limit | Status |
|---|---|---|---|---|---|

Use real run identifiers once launched; planned agents are labeled planned. Context values
include measured/estimated/unknown and freshness. Show the active batch, queued work, and exploration/hardening stage. Explain which
uncertainty an experiment resolves, the evidence for coherence, and why hardening starts.
Status vocabulary: planned, awaiting effort decision, running, blocked, verifying,
integrating, complete, handed off. Before dispatch, distinguish recommended effort from
approved effort and show the user's choice or covering policy. Group new effort decisions
by batch; preserve approvals across handoffs. Explain any proposed change before applying it.

Explain planning, dispatch, blockers, changed decisions, verification, integration, and handoff.
During long work provide a concise heartbeat, normally within 60 seconds when the runtime
permits, without claiming progress that did not occur. Include what is being resolved next.
Do not issue updates for every tool call or repeat the entire board without a meaningful change.

Escalations to the human state the decision, why evidence cannot settle it, alternatives,
consequences, and recommendation. Highest-level direction and consequential uncertain
tradeoffs and uncovered subagent effort choices belong to the human. Routine execution, telemetry checks, and authorized handoffs do not.
Summaries give decision rationale and evidence, never hidden chain-of-thought transcripts.

## Match the explanation to the human

Keep standard terminology in technical contracts and records. Explain progress through
concrete actions and their purpose, without assuming the human knows the method's name.
For example: “I’m adding a check that reproduces the bug, so we can see whether the fix
works and catch a recurrence.” Introduce “regression test” only if the term helps the reader.
Keep explanations brief; do not turn each update into a glossary or expose private reasoning.
