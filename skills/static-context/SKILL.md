---
name: static-context
description: Design the on-disk files that decide what an AI agent loads into context — instruction files, routing docs, and the ledger set that carries project state across sessions. Use when scaffolding a repo for agent work, writing or auditing CLAUDE.md / AGENTS.md files, deciding where a fact, rule, or decision should live, or when agents keep re-deriving settled decisions or acting on stale docs.
---

# Static context management

Everything an agent knows at launch was decided before the session started, by files on disk. Static context management is designing those files — what exists, what loads when, and which file owns which fact — so every session and every subagent starts from the minimum set of high-signal tokens. The dynamic half of context management (delegating, briefing subagents, compressing reports, handing off mid-task) is the [orchestrator](../orchestrator/SKILL.md) skill's job; this skill covers what is on disk before any of that runs.

The premise: context is a finite resource with diminishing returns, not a budget to fill. Attention stretches thin as context grows, so retrieval precision degrades steadily as the window fills ([Anthropic, *Effective context engineering for AI agents*](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)). Design for minimum high-signal load per task, never for completeness.

## The load model — know when a file loads before deciding what goes in it

- **Root `CLAUDE.md`** (and every `CLAUDE.md` above cwd) loads in full at every launch. Everything in it is paid for every session.
- **`CLAUDE.md` in a subdirectory below cwd** loads when the agent reads a file in that directory. Subtree-scoped law is free until it's relevant — so put it there, never at root.
- **Skills** load on invocation or judged relevance; until then only name + description sit in context. Procedures for occasional tasks belong here, not in `CLAUDE.md`.
- **`@path` imports** expand at launch. An import is not lazy; it costs the same as pasting the file.
- **`CLAUDE.md` is context, not configuration.** It makes behavior likely, not guaranteed. A constraint that must hold gets enforcement — a hook, a pre-commit guard, a CI check — and a good guard names the violated rule and the `file:line` when it fires.

| The guidance is… | Put it in | Cost |
|---|---|---|
| True every session (build commands, layout, conventions) | root `CLAUDE.md` | every launch |
| Scoped to one subtree | that subtree's `CLAUDE.md` | when files there are read |
| A procedure for an occasional task | a skill | when invoked |
| A hard constraint | a hook / guard script | enforced, not suggested |

## One home per fact

The rule everything else serves: **every fact has exactly one home file, and every other mention is a pointer to it.** Duplicated facts drift, and two files disagreeing is worse than either alone — the agent picks one arbitrarily and you don't control which.

Make the home *decidable*, not discoverable: the map file carries a "where a new fact goes" table so nobody guesses. For example: made a decision → the rulings ledger; a task or today's state → the handoff; a new term → the glossary; a contract change → the contract doc, with a version bump; anything still true next month → `docs/`; "where is X?" → the map itself.

## The ledger set — one job per root file

A small fixed set of root files, each admitting exactly one kind of content, each capped. The set that has held up:

| File | Job | Discipline |
|---|---|---|
| the map (`README.md`) | answers "where is X?" and nothing else | one row per surface; carries the where-a-new-fact-goes table |
| agent law (`CLAUDE.md`) | how agents work in this repo | pointer-style, identity-first, short; content lives in the pointed-at files |
| the handoff | today's state + the open-work queue | hard cap (~100 lines); nothing evergreen; finished work leaves the same day |
| the rulings ledger | dated decisions, newest first: the call, **why**, and what it supersedes — plus an OPEN list of undecided questions at the top | settled means settled: no session re-derives or relitigates a dated ruling |
| the glossary | the project's shared vocabulary, term by term | look a term up before coining a new one |
| `docs/` | evergreen reference — anything still true next month | one file per subject; the map points at each |
| the history | the narrative record: what happened, when, and why | where finished work from the handoff goes to rest |

The startup read is the map + the handoff + the OPEN list, and the three together stay under a few hundred lines. Everything else is reached by pointer, on demand.

The rulings ledger is the highest-leverage file in the set. Without it every session re-derives old decisions, and sometimes decides differently. Superseded entries stay in the file, marked as superseded — "we tried that, and here is why it lost" is the expensive half of the knowledge.

## Self-describing subtrees

Any directory agents work in without reading the whole repo needs three things:

- **A routing file** (`README`/`MAP`) — the mandatory first read. It says what's here and which child owns what. Agents orient at the nearest routing file and descend; they never orient at repo root and grep.
- **Local law** — a `CLAUDE.md` carrying only the rules that bind here. It loads exactly when a file in the directory is read: free until relevant.
- **A state file** — which files here are canonical and which are superseded, rewritten in place. **Updating it is the last act of every pass that writes in the directory.** A stale state file misroutes every later agent, which costs more than any single piece of work saved by skipping the update.

Create all three when the directory is commissioned, before the first work lands — not retroactively.

## Freshness is a write discipline, not a cleanup task

Static context is only as good as its last update, so updates bind to the work instead of to a schedule:

- **Docs ride the work's own commit.** A fact your change invalidated is updated in its home file in the same commit, never "in a follow-up."
- **Dead plans get a DONE / SUPERSEDED header the day they die.** Live-voice text about dead work misroutes every later reader.
- **Finished work is evicted from the handoff** to the history file, leaving one line and a pointer.
- **Sweep for drift at boundaries.** At the end of each batch of work, re-check every doc surface for stale claims, contradictions, and dead pointers — a subagent can run the whole sweep.

## Writing instructions that hold

- Under ~200 lines per instruction file; subtree files far shorter. Length reduces adherence, not just budget.
- Verifiable beats vague: "handlers live in `src/api/handlers/`" over "keep files organized"; "run `npm test` before committing" over "test your changes."
- Headers and bullets — agents scan structure the way readers do.
- Audit across files for contradictions; consistency is part of the architecture.
- If a repo already uses `AGENTS.md`, make `CLAUDE.md` an `@AGENTS.md` import or a symlink. One source, two toolchains — never two maintained copies.

## Smells

- The same fact in two files, disagreeing.
- A root `CLAUDE.md` past ~200 lines, or explaining the product in paragraphs instead of pointing.
- A session's first hour spent re-deriving a decision someone already made.
- Something in the handoff that was true last month — evergreen content in the today-file.
- A directory whose purpose you can only learn by opening its files.
- A "hard rule" that exists only as prose. Rules that must hold are hooks.
