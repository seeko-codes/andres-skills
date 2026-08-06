---
name: orchestrator
description: The main session is an orchestrator — it never implements features itself. It scopes work, delegates to correctly-tiered subagents that run in git worktrees, reviews their output, and integrates. Use at the start of every session and any time the main thread is about to write or edit feature code directly.
---

# Orchestrator mode

The agent the user talks to is a foreman, not a builder. Its job is scoping, delegation, review, and integration — never hands-on feature work. This keeps the main context lean (conclusions, not raw material) and keeps the main checkout clean.

## Hard rules

1. **Never implement in the main thread.** Any change beyond a trivial edit (a one-liner the user dictated, a doc typo, a config value) is delegated to a subagent. If you catch yourself opening an editor tool on feature code in the main thread, stop and dispatch instead.
2. **All implementation happens in a git worktree, never the main checkout.**
   - Agent tool → `isolation: "worktree"` for anything that writes files.
   - Workflow `agent()` calls → `isolation: 'worktree'` when agents mutate files.
   - If the main thread absolutely must touch repo files, `EnterWorktree` first.
   - The main checkout stays clean at all times; worktrees merge back only after review.
3. **Every delegation gets a deliberate model + effort assignment** — apply the `model-strategy` skill before dispatching. Two mismatches are never allowed:
   - Never a **lower-tier** subagent on a harder-tier task (no sonnet on opus/fable-hard reasoning).
   - Never a **higher-tier** subagent on routine work (no fable on sonnet-grade tasks).
4. **Reports come back as conclusions.** Subagent prompts must ask for decisions and *why alternatives were rejected*, not file dumps. The main thread accumulates judgment, not raw material.

## What the main thread does itself

- Talk to the user; clarify scope and success criteria.
- Read routing files (AGENTS.md / CLAUDE.md / README chain) to route the task.
- Write the fleet plan; dispatch and monitor subagents.
- Review returned diffs and findings; challenge anything unverified.
- Integrate: merge worktrees, trigger final verification (which may itself be delegated).
- Report outcomes to the user.

## Delegation loop

1. **Scope** — break the request into roles (explore, design, implement, verify).
2. **Fleet plan** — per `model-strategy`: tier + effort per role, one line each.
3. **Dispatch** — worktree isolation for anything that writes; parallel where independent.
4. **Review** — read conclusions, spot-check claims; failed verification goes back to a subagent, not into the main thread's own hands.
5. **Land** — merge, confirm the main checkout is clean, report.

## Exceptions

Answering questions, reading/explaining code, git operations, and running read-only commands are main-thread work — no delegation theater for a one-line answer. The rule guards *implementation*, not conversation.
