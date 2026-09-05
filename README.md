# Andres' Skills

A curated set of agent skills from my daily setup. Each skill is a Markdown instruction
file, sometimes with supporting references or a helper script. This repo is a portable
selection, not a backup of my local agent configuration.

The main change in this edition is selective delegation. `orchestrator` keeps decisions
in the main session and delegates only when a bounded result saves more context than its
brief and review cost. `lean-quality` now governs implementation; `tdd` remains available
by explicit request.

## Install

Clone the repo, then choose the skills you want:

```bash
git clone https://github.com/seeko-codes/andres-skills.git
mkdir -p ~/.claude/skills
cp -R andres-skills/skills/* ~/.claude/skills/
```

The copy command installs the full collection for Claude Code. For one project, use that
repo's `.claude/skills/` instead. Back up any same-named local skills before copying,
because this overwrites matching files. It does not remove obsolete files from an older
installation.

The orchestration instructions also include Codex and Pi adapters. Install into the skill
directory supported by your runner. Model IDs, effort settings, and dispatch controls are
resolved from the active session, not copied from my machine.

Install `orchestrator`, `model-strategy`, and `lean-quality` together. The other skills can
be used independently. Optional references to `curious` and `unslop` do not require those
skills; the bundled instructions include the fallback procedure.

## The skills

| Skill | What it does | When to use it |
|---|---|---|
| [orchestrator](skills/orchestrator/SKILL.md) | Keeps connected decisions in the main session; delegates bounded reading, execution, and independent review | Context-heavy work or independent slices where delegation pays |
| [model-strategy](skills/model-strategy/SKILL.md) | Maps task risk and verifiability to available models and effort settings | After deciding to delegate, before launching a child |
| [lean-quality](skills/lean-quality/SKILL.md) | Red-green-refactor, property checks, strict types, dead-code checks, and verification before committing | Writing or changing production code after the design is settled |
| [tdd](skills/tdd/SKILL.md) | Behavior-first vertical slices with references on tests, interfaces, mocking, and refactoring | Explicit `/tdd` requests; automatic implementation work uses `lean-quality` |
| [grill-with-docs](skills/grill-with-docs/SKILL.md) | Challenges a plan one question at a time and records surviving terminology and decisions | Stress-testing a plan against project docs |
| [diagnose](skills/diagnose/SKILL.md) | Reproduce, minimise, hypothesise, instrument, fix, and regression-test | Bugs where guessing has not worked |
| [wait-what](skills/wait-what/SKILL.md) | Re-explains an answer with context and the project's vocabulary | Explicit `/wait-what` requests only |

`wait-what` is by [Matt Pocock](skills/wait-what/NOTICE.md), preserved verbatim with its
[MIT license](skills/wait-what/LICENSE). Its attribution files are part of the skill.

## How they fit together

```text
grill-with-docs       Challenge the plan and record decisions.
orchestrator          Decide what stays local and what can delegate.
  model-strategy      Select available capability and effort for each child.
  lean-quality        Build settled changes test-first.
diagnose              Establish a reproduction before fixing a bug.
tdd                   Optional, explicitly requested TDD reference.
wait-what             Ask for a clearer explanation.
```

Small tasks stay local. For larger work, the main session freezes the contract, assigns
disjoint writes to isolated worktrees, reviews results, and checks that the combined
changes work. Each child gets a bounded brief and a checkable completion condition.
Children do not delegate again.

The tier names in `model-strategy` are policy labels, not model IDs. They must be mapped
to models the current runner actually exposes. The policy favors a capable model for
connected or consequential work and reserves weaker models for work with reliable
checks. See [the validation notes](skills/model-strategy/EVIDENCE.md) before changing
that mapping.

## What is different from my local setup

- No private project paths, installed profile roster, or machine-specific model IDs.
- Native dispatch adapters rather than a required vendor's agent runner.
- Optional inquiry and writing skills have an inline fallback.
- The public diagnostic script retains its interactive-terminal guard. A human runs it
  in their own terminal and pastes the captured output back.
- Existing third-party files and notices stay intact.

Local skill changes are reviewed before publication. A newer local file is not
automatically better for this repo, particularly when it removes a portability fix or
introduces a dependency that is not included here.

## Lavish, an optional companion

Lavish is a separately installed CLI, not one of this repo's skills. It turns an HTML
artifact into a browser page that a user can annotate and send back to the agent.
The collection works without it.

If it is already installed, the basic review loop is:

```bash
lavish-axi playbook plan
lavish-axi .lavish/plan.html
lavish-axi poll .lavish/plan.html
```

Write the HTML file before opening it. Read the matching playbooks before creating the
artifact. `poll` waits for submitted feedback or the user ending the session; keep it
tracked so feedback returns to the agent. Use this loop when the user asks for visual
review, not as a mandatory step before every task.

`lavish-axi share` uploads to a third-party host and is public by default. Local review
does not require sharing. Do not publish project content without the user's approval.

## Writing your own

A skill folder needs a `SKILL.md` with YAML `name` and `description` fields. State the
requests that should trigger it. Keep the main file focused on the procedure and put
conditional detail behind links to supporting files. Include those files when distributing
the skill, and check that it can run without your private paths or unbundled dependencies.

## License

[MIT](LICENSE). `skills/wait-what/` carries its own MIT copyright and
[provenance notice](skills/wait-what/NOTICE.md).
