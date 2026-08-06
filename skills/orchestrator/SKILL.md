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

## Decomposition: batches as a basis

Split a feature the way a basis spans a space. A **batch** is a set of subagents that together are:

- **Spanning** — the union of their slices delivers the entire feature; nothing falls between agents.
- **Independent** — disjoint *write-sets*: no two slices in a batch write the same files, so merges never collide. Reading shared code is free; only writes must be disjoint.

Each slice is **vertical** — an end-to-end unit of the feature, not a horizontal layer. Verticality is scale-relative and recursive: when a slice splits, its pieces are vertical with respect to *that slice's* deliverable, not the original feature — layers never become the right split at any depth.

Rules:

1. **No dependencies between slices** → one batch, all slices dispatched in parallel worktrees.
2. **Dependencies** → topologically sort into batches: each batch is internally parallel; the next dispatches only after the previous one has merged and verified.
3. **Orthogonalize before you parallelize.** Shared seams (types, schemas, contracts, route registries) are where slices would collide. Extract them into a small **contract batch** dispatched first; later slices build against the frozen contract.
4. **Context budget: ~100k tokens per agent** — its repo reading + instructions + work must fit in the smart zone. A slice too big to fit splits along another vertical seam; if it can't split without breaking independence, it becomes its own sequential batch.
5. **Batch boundary ritual:** merge all worktrees, verify the *composed* result (spanning of tasks doesn't guarantee the composition works), then plan the next batch against the new base.
6. No-redundancy binds *construction* only — verification fleets are deliberately redundant and stay that way.

## Delegation loop

1. **Scope** — break the request into vertical slices; sort into batches per the basis rules above.
2. **Fleet plan** — per `model-strategy`: tier + effort per role, one line each.
3. **Dispatch** — worktree isolation for anything that writes; the current batch runs fully parallel.
4. **Review** — read conclusions, spot-check claims; failed verification goes back to a subagent, not into the main thread's own hands.
5. **Land** — merge the batch, verify the composition, confirm the main checkout is clean; next batch or report.

## Exceptions

Answering questions, reading/explaining code, git operations, and running read-only commands are main-thread work — no delegation theater for a one-line answer. The rule guards *implementation*, not conversation.
