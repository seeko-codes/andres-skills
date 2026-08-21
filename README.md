# Andres' Skills

A small, battle-tested set of skills for [Claude Code](https://claude.com/claude-code) — pulled straight from my daily setup, with the machine-specific stuff stripped out. Each one is mostly a plain-Markdown instruction file (plus the occasional helper script) that the agent loads when the moment calls for it.

The headliner is **orchestrator**: it turns your main Claude session into a foreman that never writes feature code itself — it scopes work, delegates to the right-sized subagents in isolated git worktrees, reviews what comes back, and integrates. The other six are the skills I reach for most, and they compose with it. An eighth, **wait-what**, isn't mine — it's [Matt Pocock's](https://github.com/mattpocock/skills), republished here verbatim under MIT.

## Install

```bash
git clone https://github.com/seeko-codes/andres-skills.git
mkdir -p ~/.claude/skills
cp -R andres-skills/skills/* ~/.claude/skills/
```

That's it — `~/.claude/skills/` makes them available in every project. For a single project, copy them into that repo's `.claude/skills/` instead. Restart your Claude Code session and the skills register automatically; invoke one explicitly with `/orchestrator`, `/tdd`, etc., or just work normally and let them trigger on their own. The exception is `wait-what`, which only ever runs when you type it.

That covers the skills. One companion tool — [Lavish](#lavish-the-companion-tool) — is not a skill and installs separately.

## The skills

| Skill | One-liner | Fires when… |
|---|---|---|
| [orchestrator](skills/orchestrator/SKILL.md) | Main session delegates everything; implementation happens in worktree-isolated subagents | a session starts, or the main thread is about to edit feature code |
| [model-strategy](skills/model-strategy/SKILL.md) | Deliberately assign a model tier + reasoning effort to every subagent before spawning | any multi-agent fan-out, workflow, or delegation |
| [tdd](skills/tdd/SKILL.md) | Red-green-refactor with behavior-first vertical slices | building features or fixing bugs test-first |
| [grill-with-docs](skills/grill-with-docs/SKILL.md) | Relentless one-question-at-a-time interview that stress-tests a plan against your project's own docs, updating the glossary and ADRs as decisions land | you want a plan challenged, not implemented |
| [diagnose](skills/diagnose/SKILL.md) | Disciplined debugging loop: reproduce → minimise → hypothesise → instrument → fix → regression-test | something is broken and guessing hasn't worked |
| [static-context](skills/static-context/SKILL.md) | Reorganize an existing repo's on-disk context — one home per fact, a capped ledger set, dead text marked dead — so agents stop loading stale or duplicated docs | docs have sprawled, CLAUDE.md keeps growing, or every session re-derives old decisions |
| [learning-with-ai](skills/learning-with-ai/SKILL.md) | Flips the agent from answering to teaching, grounded in how encoding works: the learner performs the operations, the agent supplies questions, sequence, and checks | you're learning or studying through the agent, or building a product that teaches |
| [wait-what](skills/wait-what/SKILL.md) **· third-party** | Tells the agent its last message didn't land, and to re-pitch it with context, in Simplified Technical English, using the project's own vocabulary | never by itself — `disable-model-invocation: true` means the model can't self-trigger it; you type `/wait-what` |

**Third-party credit:** `wait-what` is by **[Matt Pocock](https://github.com/mattpocock/skills)**, republished verbatim from his `mattpocock-skills` plugin (v1.2.3) under MIT. It's kept as his file rather than reworded into mine so the credit stays where it belongs — copyright and provenance travel with it in [`skills/wait-what/LICENSE`](skills/wait-what/LICENSE) and [`skills/wait-what/NOTICE.md`](skills/wait-what/NOTICE.md). Everything else here is mine.

## How I actually use them

**orchestrator** — the always-on one. My main session stays a clean thread of decisions while subagents do the building in git worktrees. The payoff is twofold: the main checkout never gets dirty, and the main context stays small enough to hold a whole project conversation without drowning in file dumps. Work is decomposed into *batches* — spanning, independent sets of vertical slices, like basis vectors of the feature — and the full theory has [a repo of its own](https://github.com/seeko-codes/orchestrator-skill).

**model-strategy** — loaded before every fleet I dispatch: a three-book parallel-read pipeline, a screenshot-review fleet, corpus inventory sweeps over hundreds of lesson files. The rule that pays rent: the ladder is haiku < sonnet < opus < fable, mismatches are forbidden in both directions, and every effort upgrade past medium has to be argued for — benchmark cost curves show max effort buys a few points for a multiple of the price.

**tdd** — how the real features get built: a replay-harness and optimizer package for my tutoring engine, an ontology/layout module for a diagnostics page. Vertical slices over horizontal ones — test a behavior end-to-end, not a layer at a time.

**grill-with-docs** — the plan killer. I used it to interrogate a diagnostic-analysis page design before delivery and to pressure-test who my app's target user actually is. It asks one question at a time until the plan survives or dies, and writes the surviving decisions into CONTEXT.md and ADRs so they stick.

**diagnose** — for the bugs where "just look at it" already failed. The discipline is the point: no fix until there's a reproduction, no hypothesis without instrumentation to confirm it, and the instrumentation all comes back out afterward.

**static-context** — the other half of context management. Orchestrator governs what a session *does* with its context; static-context governs what's on disk before the session starts. It's written for the repo you already have, not a greenfield one: an inventory-classify-migrate pass that gives every fact one home file, marks dead plans dead, shrinks the instruction files to pointers, and leaves a ledger set — a map, a capped handoff, a dated rulings file — that lets a fresh session pick up a months-long project without re-deriving anything. Distilled from running a multi-month, many-agent project on exactly that file discipline.

**learning-with-ai** — the odd one out: it doesn't manage the agent's work, it changes how the agent treats *you* when you're the one learning. It's built on a mechanism, not a vibe: encoding follows the operations the learner performs, and an AI is the cheapest outsourcing machine ever built for exactly those operations — so the skill makes the agent demand an attempt before it answers, give hints that point instead of state, critique the structure the learner builds rather than supplying its own, and refuse to count "makes sense" as learned. Distilled from building an AI tutoring product on the learning-science literature; the full encoding model rides along in `encoding.md`.

## How they fit together

```
static-context        — the files on disk every session starts from
orchestrator          — the main session's operating mode
   └─ model-strategy  — picks each subagent's model + effort
        └─ tdd        — how implementation subagents build
grill-with-docs       — before committing to a plan
diagnose              — when something breaks anyway
learning-with-ai      — when you're the student, not the shipper
```

A typical feature: grill the plan first, then the orchestrator splits it into roles, model-strategy prices each role, implementation lands test-first in a worktree, and the main thread reviews and merges.

## Lavish: the companion tool

The one non-skill piece of my setup, and the only thing here that isn't plain Markdown. [Lavish](https://www.npmjs.com/package/lavish-axi) is a third-party CLI — not part of this repo, not maintained by me — that turns an HTML artifact into a review surface I can annotate in the browser and send back to the agent.

### Install

```bash
npm install -g lavish-axi
```

Then wire it into Claude Code as a `SessionStart` hook in `~/.claude/settings.json`:

```json
{
  "hooks": {
    "SessionStart": [
      {
        "matcher": "",
        "hooks": [
          { "type": "command", "command": "lavish-axi", "timeout": 10 }
        ]
      }
    ]
  }
}
```

The `lavish-axi` binary is a hard requirement. Without it there is no hook output, no review server, and nothing below happens — this isn't a nice-to-have layer over some fallback.

### Why it's a tool, not a skill

A skill is a folder in `~/.claude/skills/` that gets loaded when its description matches what you're doing. Lavish doesn't need that machinery: run the binary bare and it prints its own description, visual guidance, playbook index and help text, and the `SessionStart` hook pipes exactly that into every session. It self-advertises once per session instead of waiting to be matched. So cloning this repo gets you the eight *skills*; Lavish you install yourself. (The npm package does ship a `SKILL.md` of its own — with the hook wired up you don't need it, and I don't use it.)

### The loop

1. The agent writes an HTML artifact — by default under `.lavish/` in the working directory.
2. `lavish-axi <html-file>` serves it locally and opens it in the browser.
3. I annotate elements and selected text, and queue prompts against what I annotated.
4. `lavish-axi poll <html-file>` long-polls and returns that feedback to the agent. It stays silent until I send or end the session, so it just sits there running.

Guidance comes from playbooks fetched with `lavish-axi playbook <id>` — `diagram`, `table`, `comparison`, `plan`, `code`, `input`, `slides` — and `lavish-axi design` returns the design router plus CDN snippets. Other verbs worth knowing: `end` (agent-side close), `export` (standalone HTML with local assets inlined), `stop` (shut the background server down).

### How I actually use it

The `plan` playbook, mostly, and always at the same moment: before a fleet goes out. Instead of a wall of chat text, the orchestrator renders the fleet plan as a page — goal, current state, proposed approach, the batch decomposition as a Mermaid diagram, risks and open questions at the end. Then I click the slice I don't believe and annotate it — "this writes the same files as slice 2, they're not independent" — queue it, and `poll` hands that straight back. Catching a collision by pointing at a box beats catching it by re-reading a transcript.

The `input` playbook does the other half: radio groups and a submit button for decisions the agent needs from me. A scope-triage pass that would have been a dozen one-at-a-time chat questions becomes a page of choices and one Send.

**Warning:** `lavish-axi share <html-file>` publishes the artifact to `ht-ml.app`, a third-party host, and shares are **public by default** — anyone with the link can open it. `--password` publishes a private password-protected page instead. Think before sharing an artifact that quotes your codebase.

## Writing your own

Skills are just folders with a `SKILL.md` — YAML frontmatter (`name`, `description` with explicit "use when" triggers) plus instructions. The description is the only thing the agent sees when deciding whether to load a skill, so put the trigger words there. Keep the body short — around 120 lines at most — and split anything bigger into sibling reference files, like `tdd/` does here.

## License

MIT — see [LICENSE](LICENSE).

One exception: `skills/wait-what/` is a third-party work under a separate copyright — MIT, Copyright (c) 2026 Matt Pocock. Its licence and provenance live with the skill, in [`skills/wait-what/LICENSE`](skills/wait-what/LICENSE) and [`skills/wait-what/NOTICE.md`](skills/wait-what/NOTICE.md).
