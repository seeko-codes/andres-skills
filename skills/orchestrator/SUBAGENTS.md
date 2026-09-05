# Native subagent operating guide

The work contract is harness-independent. Use the active session's native tools; do not
require another harness, migrate sessions, or ask approval merely to change runner names.

Use general-purpose native agents. The brief supplies each run's temporary role through
its question, corpus, permissions, and verifier. Runtime profile names are optional
adapters, never a mandatory taxonomy. Read/write and model capability differences remain
explicit. Fresh context, not a specialist label, makes a review independent.

Give every agent the full toolset the active harness makes available. Do not apply
role-based tool allowlists or remove tools for a reading or review assignment. A brief can
bound the work and which files may change without disabling tools. Narrow tool access only
when the user explicitly requests it or the harness itself enforces a restriction.

## What stays fixed

- Main owns scope, decisions, frozen contracts, and acceptance.
- Each child gets a bounded question or write-disjoint slice, an exact input corpus, a
  verifier, and the instruction "Subagents never delegate."
- Writing children use isolated git worktrees. Prefer native managed isolation. When the
  runner lacks it, create a worktree explicitly and put its absolute path in the brief.
  Fail closed if isolation fails. Gitignored-only work uses the documented exception.
- Children follow `lean-quality` for code. Write concise conclusions with concrete evidence;
  use `unslop` for writing if separately installed. Open requirements stop
  execution and return to the main session. Review and composed verification precede merge.
- Completion means verified committed work or the explicitly commissioned local artifact.
  Track the run through native completion and messaging controls, not detached shell jobs.

## Resolve only the active adapter

### Codex

Inspect the live native subagent schema, commonly `collaboration.spawn_agent` or
`spawn_agent`. Use its matching message, wait, status, and interrupt tools. There is no
requirement for Pi profiles or a Pi registry call. Use supported model/effort fields only;
otherwise report parent inheritance. Full-history forks may forbid model overrides.

Children may share cwd and files. A spawn is not proof of isolation. For each writing
child, create a distinct worktree first or make verified worktree creation its first step.
Name the absolute worktree path and require commands and edits to stay there. Put local
configuration artifacts outside the product checkout in a bounded staging directory when
that is the commissioned output; installing to protected paths still needs tool approval.

### Claude

Use the native Agent/Task tool exposed in the session. Use managed worktree isolation when
supported, otherwise create explicit worktrees. Use native background completion and resume
controls. Do not require Codex or Pi tools, profile files, or model ids.

### Pi

Use the native `subagent` tool. Only here, read [PI-RUNTIME.md](PI-RUNTIME.md) for registry,
workflow, managed worktree, and FleetView examples; verify them against the live schema.

## Missing capabilities

A missing vendor-specific tool is irrelevant when a native equivalent preserves the
contract. If there is no native delegation at all, keep eligible work local or report the
actual missing capability. Never silently discard isolation or review to keep dispatching.

Model strategy fixes capability and effort from risk, not price. Print only what the live
harness exposes. A profile path or exact effort is not required when the harness hides it.
