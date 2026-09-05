---
name: model-strategy
description: Choose installed subagent models and reasoning effort from task difficulty, consequence, and verifiability. Use whenever launching subagents, workflows, fan-outs, reviewers, or worktree agents.
---

# Model strategy

This skill does not decide whether to delegate. The orchestrator's activation gate decides that first.
Load model strategy only after a subagent has a paying question, frozen slice, or review target.

Use a small, strong fleet. Optimize expected correctness and decision quality, not token price or
agent count. One capable agent holding the connected problem is usually better than several weaker
agents exchanging summaries.

Read [EVIDENCE.md](EVIDENCE.md) when changing this policy or when the installed model family
changes.

## Verify availability first

1. Inspect the active harness's native dispatch schema and available model metadata. Use
   registry discovery only when the live tool provides it. The tool schema itself is the
   authority in harnesses without an agent-profile registry.
2. Record the selected model, effort, tools, and write access where exposed. Spot-check a
   profile definition only when the native runner actually uses one. Unknown or inherited
   metadata must be labeled as such, not inferred from another harness's profile files.
3. Select only model and effort controls accepted by the current tool. Prefer the capable
   parent model when native children inherit it. Harness-specific syntax belongs in that
   harness's adapter, never in an implementation brief's requirements.
4. Use native Codex subagents in Codex, native Claude agents in Claude, and native Pi
   subagents in Pi. A different runner does not change the task or require permission to
   substitute. Preserve isolation, review, and completion checks across all three.

## Keep the three controls separate

- **Base model** determines learned capability. More reasoning cannot reliably supply knowledge or
  strategies outside that model's reach.
- **Reasoning effort** controls how much internal reasoning the selected model may use. It improves
  search, checking, and multi-step work within that model's capabilities.
- **Curiosity procedure** improves inquiry direction. Rank open questions, predict before reading, consolidate findings, and check for
  surprises. This procedure does not change the base model or its reasoning allowance.

Do not prompt a reasoning model to reveal private chain of thought. Ask for conclusions, evidence,
checks, and concise rationale. Use the curiosity protocol to organize external inquiry.

## Assignment, not persona

Select general-purpose agents. A brief's context and question define the role for that
run; profile labels do not confer expertise. Model strength and available read/write
tools still matter. Do not select tool-restricted profiles merely to satisfy a fixed
worker/explorer/reviewer taxonomy. An independent
review needs separate context and an adversarial brief, not a special profile name.

Give every agent the full toolset the active harness makes available. Do not apply
role-based tool allowlists or remove tools for a reading or review assignment. A brief can
bound the work and which files may change without disabling tools. Narrow tool access only
when the user explicitly requests it or the harness itself enforces a restriction.

## Choose the model before the effort

The labels **strong-tier**, **standard-tier**, and **mechanical-tier** describe this
policy's assignments, not provider model IDs. Map them to models actually exposed by the
active runner. Never pass these labels as model parameters. If only the parent model is
available, use it and report inheritance. Validate each mapping on representative tasks.

Choose **strong-tier by default** when any of these is true:

- requirements or design decisions remain open;
- the work joins several files, concepts, systems, or sources;
- failure is hard to detect, costly, or likely to look plausible;
- the task is architecture, planning, research synthesis, ambiguous debugging, security, migration,
  adversarial review, or final integration;
- the agent must notice that the brief itself is wrong.

Choose **standard-tier only for bounded execution** when all of these are true:

- the contract and success criteria are frozen;
- the relevant context is local and familiar;
- few judgment calls remain;
- tests, types, schemas, or another strong verifier can reject a wrong result;
- a strong-tier reviewer owns the consequential gate.

Choose **mechanical-tier only for mechanical work** when the output can be checked exactly: file inventory,
literal extraction, deterministic reformatting, generated lists, or running a specified command. If a
plausible but wrong answer could pass unnoticed, mechanical-tier is below the capability bar.

When uncertain between tiers, move up. Do not replace one strong-tier agent with several standard-tier or mechanical-tier agents.

## Choose effort within the model

Use only settings exposed by the current runner. The labels below are policy guidance,
not a claim that every provider accepts them. Report inherited or unavailable effort honestly.

- **low**: exact retrieval, simple execution, or a short tool sequence with a strong verifier. Mechanical work
  stays here. Do not use low for interpretation or consequential production work.
- **medium**: default for bounded implementation and ordinary agentic work. This is the minimum for
  standard-tier production code and strong-tier work whose decisions are already settled.
- **high**: complex debugging, planning, research, connected implementation, and high-value
  judgment. This is the normal strong-tier setting for exploration.
- **xhigh**: difficult security or code review, deep research, and long-running agentic work where
  representative checks show a gain over high.
- **max**: one hardest quality-first gate after xhigh proves insufficient. Do not make max a ritual.

Use effort to deepen a capable model, not to rescue an underpowered choice. Prefer strong-tier/medium over
standard-tier/high for unresolved judgment. Standard-tier/high can beat strong-tier/low on some in-capability, verifiable tasks,
but that is an evaluation result to prove, not a routing assumption.

## Shape the fleet

- Run the orchestrator on the strongest installed general model, using an accepted
  effort setting suited to judgment.
- Keep connected work with one strong-tier agent.
- Parallelize only independent questions or write-disjoint slices.
- Use standard-tier for the routine residue after strong-tier or the main session freezes the contract.
- Use mechanical-tier through scripts whenever possible; a deterministic command is better than a mechanical
  model call.
- Review consequential work with an independent strong-tier context. Different context and an adversarial
  lens create de-correlation; a weaker reviewer does not create useful independence if it misses the bug.

## Fleet plan

Before dispatch, print only what is needed:

```text
Available: <agent>=<exact model>/<effort>, ...
Plan:
- <paying question or frozen slice> -> <agent>/<model>/<effort> because <task property>
Quality gate: <independent check or reviewer>
```

A fleet plan fails if it routes judgment to mechanical-tier, uses standard-tier because it is cheaper, fans out a connected
problem, or raises effort without first checking that the base model fits the task.
