# Andres' Skills

A curated set of agent skills from my daily setup. Each skill is a Markdown instruction
file, sometimes with supporting references or a helper script. This repo is a portable
selection, not a backup of my local agent configuration.

The central idea is to give each agent a clear job and just the information it needs.
A capable manager keeps track of the whole goal. A small team handles focused pieces,
working at the same time when those pieces do not depend on each other.

The instructions use established technical terms so agents can apply methods precisely.
This README explains the logic without requiring you to know those terms first.

## Install

Clone the repo, then choose the skills you want:

```bash
git clone https://github.com/seeko-codes/andres-skills.git
mkdir -p ~/.claude/skills
cp -R andres-skills/skills/* ~/.claude/skills/
```

The legacy `diagnose` skill has been removed. If you previously installed it, remove only
that old installed folder after checking for your own edits; copying this version will not
remove it automatically.

The copy command installs the full collection for Claude Code. For one project, use that
repo's `.claude/skills/` instead. Back up any same-named local skills before copying,
because this overwrites matching files. It does not remove obsolete files from an older
installation.

The orchestration instructions also include Codex and Pi adapters. Install into the skill
directory supported by your runner. Model IDs, effort settings, and dispatch controls are
resolved from the active session, not copied from my machine.

Install `orchestrator`, `model-strategy`, and `lean-quality` together. The other skills can
be used independently. `grill-with-docs` supports human decisions; `wait-what` supports
clearer explanations.

## The skills

| Skill | What it helps you do |
|---|---|
| [orchestrator](skills/orchestrator/SKILL.md) | Split a large goal into focused jobs, keep track of progress, and check the pieces work together. |
| [model-strategy](skills/model-strategy/SKILL.md) | Choose a suitable model and propose how much reasoning effort each helper needs. You approve the effort. |
| [lean-quality](skills/lean-quality/SKILL.md) | Once the arrangement makes sense, strengthen the implementation with checks for behavior, mistakes, and integration. |
| [tdd](skills/tdd/SKILL.md) | When you request test-driven development or `/tdd`, build one behavior at a time: first a failing check, then working code, then cleanup. |
| [grill-with-docs](skills/grill-with-docs/SKILL.md) | Keep project direction in your hands: clarify goals and tradeoffs one question at a time, then record your decisions. |
| [wait-what](skills/wait-what/SKILL.md) | When you request `/wait-what`, explain the previous answer again with enough background to follow it. |

`wait-what` is by [Matt Pocock](skills/wait-what/NOTICE.md), preserved verbatim with its
[MIT license](skills/wait-what/LICENSE). Its new reference shelf is a collection-maintained supplement.

## How work moves forward

1. **Understand the whole goal.** You own the purpose, priorities, and consequential tradeoffs.
   Use `grill-with-docs` when those need discussion: the agent investigates and recommends,
   you decide. Record the result and what would count as success.
2. **Check the arrangement.** Explore alternatives with small experiments. Investigate the
   assumption most likely to make later work unnecessary or wrong. Preserve existing protections.
3. **Give each helper a complete, focused job.** Include the relevant requirements, files,
   constraints, and checks. Keep decisions that change together with one owner. The pieces
   should be easy to replace.
4. **Do ready work together.** If one job needs another's result, queue it for a later batch.
   Repeated back-and-forth between helpers is a reason to reconsider the split.
5. **Strengthen the chosen implementation.** Once responsibilities and connections make sense,
   apply lean-quality to the code being kept. Check existing behavior; use test-driven
   development for new behavior and fixes. Choose checks for the actual risk and project
   requirements; there is no mandatory tool stack for every edit. For a screen, try its
   interactions and inspect screenshots.
6. **Check the whole result.** A helper finishing does not mean the feature works. The manager
   combines the pieces, checks the agreed outcome, and updates the next batch.

In the technical instructions, the whole goal is the **horizontal slice** and each focused
contribution is a **vertical slice**. Together, all batches must cover the goal, including
the work of combining and checking their outputs. The basis-vector analogy is a planning
aid, not a mathematical guarantee of correctness.

Small tasks stay with one agent. For larger tasks, delegation can provide specialization,
keep the manager's working context manageable, and allow useful parallel work.

## What you control and see

Managers use the strongest available model at maximum supported reasoning effort. Helpers
can use the same capability or less when appropriate. Before launching them, the manager
proposes effort settings with reasons and tradeoffs for your approval. An approval can cover
a whole batch or a stated policy; it carries forward within that scope. Changes outside it
come back to you. The agent reports settings it cannot control honestly.

Set these options in your request or project instructions:

| Option | Default | Meaning |
|---|---|---|
| `max_context_per_agent` | `100000` tokens | Maximum working context for each agent, including managers. Tokens are units of text processed by the model. |
| `context_warning_fraction` | `0.8` | Start saving progress and replanning at 80% of that limit. |
| `wayfinder` | `false` | Enable a coordinator for a longer sequence of manager sessions. |

Context includes instructions, inputs, working history, and room for the answer; it is not
the cumulative usage bill. Passing the limit means the assignment was too large for its
budget. The manager preserves progress and narrows the remaining job. It labels usage as
measured, estimated, or unknown instead of pretending it can see unavailable measurements.

With **Wayfinder** enabled, one coordinator can manage orchestrators that each manage helpers.
Otherwise there is only one manager with helpers that cannot delegate. Automatic handoffs
depend on what the running application supports; installing a skill does not add those controls.
You keep ownership of the highest-level direction and consequential uncertain decisions.

You should see what is happening, why, who owns each job, what is waiting, and what happens
next. The manager brings worker updates into one readable view. See the technical details for
[context](skills/orchestrator/CONTEXT.md), [Wayfinder](skills/orchestrator/WAYFINDER.md),
[effort evidence](skills/model-strategy/EVIDENCE.md), and
[exploration and hardening](skills/orchestrator/doctrine/stages.md).

## References when a question comes up

Each process has a small reference shelf with authoritative definitions, original method
descriptions, or official tool instructions. Agents look up a relevant section when a specific
question blocks progress; they do not preload every source. More reading is useful only when
it resolves the uncertainty. References help ground decisions but cannot guarantee them.

Browse the shelves for [orchestration](skills/orchestrator/REFERENCES.md),
[model selection](skills/model-strategy/REFERENCES.md), [quality checks](skills/lean-quality/REFERENCES.md),
[test-driven development](skills/tdd/REFERENCES.md), [planning and decisions](skills/grill-with-docs/REFERENCES.md),
and [clear explanations](skills/wait-what/REFERENCES.md).
Each entry says which question it answers and where its advice stops applying.

## What is different from my local setup

- No private project paths, installed profile roster, or machine-specific model IDs.
- Native dispatch adapters rather than a required vendor's agent runner.
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
