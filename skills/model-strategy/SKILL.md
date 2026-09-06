---
name: model-strategy
description: Assign available models and reasoning effort to managers and bounded subagent contracts according to complexity, consequence, and verifiability.
---

# Capability allocation for a small autonomous team

The orchestrator decides scope, delegation, and context. This skill selects sufficient
model capability and effort for each assignment. Prefer fewer capable agents holding
cohesive problems; additional weak agents do not repair a poorly cut contract.

## Managers

The core orchestrator and optional Wayfinder use the smartest available general model
at the highest supported reasoning effort. This is the user's operating policy, not a
claim that maximal effort is optimal on every benchmark. Inspect actual runtime metadata
and supported controls. Do not invent rankings, model IDs, or settings. If the current
manager cannot change models/effort, report its actual configuration and limitation;
use a supported transition when available and authorized, never pretend to upgrade it.

## Subagents

Subagents may equal the manager in both capability and effort or use less when sufficient.
Choose model and effort separately based on the remaining work:

| Work | Allocation |
|---|---|
| Abstract reasoning, ambiguous investigation, architecture, consequential review | Strongest capability and high-to-maximum effort when needed |
| Connected implementation with difficult judgment | Capability and effort sufficient for that reasoning |
| Frozen local execution with a strong verifier | Lower model and effort only when reliable for the remaining work |
| Exact collection or deterministic transformation | Prefer scripts; otherwise a sufficient inexpensive model |

Do not equate execution with easy work. Consider whether the agent must detect a bad brief,
whether mistakes look plausible, their consequences, and whether checks reliably reject them.
When uncertain, route upward or resolve the ambiguity before commissioning cheaper execution.
Autonomy within the contract is compatible with a narrow context package.

## Resolve and report

Use only models and effort fields accepted by the native schema. Preserve inherited settings
honestly when overrides are absent; full-history forks may forbid overrides. Use general-purpose
agents with the available tools; a specialist name does not confer expertise. Respect user/runtime
restrictions and put task boundaries in the brief. Do not launch alternative agent CLIs.

In the centralized assignment board state actual model, effort, reason for selection, and
unknown/inherited fields. Report model choices as policy decisions, not benchmark facts.
Read [EVIDENCE.md](EVIDENCE.md) when evaluating or changing capability mappings. Validate
quality through task success, escaped defects, and rework before optimizing latency or usage.
