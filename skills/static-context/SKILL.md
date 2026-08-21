---
name: static-context
description: Reorganize an existing repo's on-disk context — the instruction files, docs, and notes that decide what an AI agent loads — so every fact has one home, stale text stops misrouting sessions, and the startup read stays small. Use when a repo's docs have sprawled, CLAUDE.md keeps growing, agents act on stale or contradictory docs, or every session re-derives decisions that were already made.
---

# Static context management

Everything an agent knows at launch was decided before the session started, by files on disk. In a repo that has been worked for a while, those files already exist — a bloated CLAUDE.md, a NOTES.md nobody prunes, three READMEs that half-agree, plans in live voice for work that shipped months ago. Static context management is **reorganizing that inventory**: same facts, new homes, nothing lost — so every session and subagent starts from the minimum set of high-signal tokens. The dynamic half of context management (delegating, briefing subagents, compressing reports) is the [orchestrator](../orchestrator/SKILL.md) skill's job; this one is about the disk.

The premise: context is a finite resource with diminishing returns, not a budget to fill. Attention stretches thin as context grows, so retrieval precision degrades steadily as the window fills ([Anthropic, *Effective context engineering for AI agents*](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)). And stale context is worse than missing context — an agent that finds nothing goes looking; an agent that finds a confident, outdated claim acts on it.

## First, the load model — placement follows mechanics

You cannot decide where a fact belongs until you know when each location loads:

- **Root `CLAUDE.md`** (and every `CLAUDE.md` above cwd) loads in full at every launch. Everything in it is paid for every session, relevant or not.
- **`CLAUDE.md` in a subdirectory below cwd** loads when the agent reads a file in that directory. Subtree-scoped rules are free until relevant — so they belong there, never at root.
- **Skills** load on invocation or judged relevance; until then only name + description sit in context. Procedures for occasional tasks belong here, not in `CLAUDE.md`.
- **`@path` imports** expand at launch. An import is not lazy; it costs the same as pasting the file.
- **`CLAUDE.md` is context, not configuration.** It makes behavior likely, not guaranteed. A constraint that must hold gets enforcement — a pre-commit guard, a hook, a CI check — and a good guard names the violated rule and the `file:line` when it fires.

| The guidance is… | It belongs in | Loads |
|---|---|---|
| True every session (build commands, layout, conventions) | root `CLAUDE.md` | every launch |
| Scoped to one subtree | that subtree's `CLAUDE.md` | when files there are read |
| A procedure for an occasional task | a skill | when invoked |
| A hard constraint | a hook / guard script | enforced, not suggested |

## The organizing rule: one home per fact

**Every fact gets exactly one home file; every other mention becomes a pointer to it.** Duplicated facts drift, and two files disagreeing is worse than either alone — the agent picks one arbitrarily and you don't control which.

Make the home *decidable*, not discoverable: the map file carries a "where a fact goes" table so nobody guesses. For example: a decision made → the rulings ledger; a task or today's state → the handoff; a term of art → the glossary; a contract change → the contract doc, with a version bump; anything still true next month → `docs/`; "where is X?" → the map itself.

## The target shape — the ledger set

A small fixed set of root files, each admitting exactly one kind of content, each capped. The set that has held up over months of heavy agent work:

| File | Job | Discipline |
|---|---|---|
| the map (`README.md`) | answers "where is X?" and nothing else | one row per surface; carries the where-a-fact-goes table |
| agent law (`CLAUDE.md`) | how agents work in this repo | pointer-style, identity-first, short; content lives in the pointed-at files |
| the handoff | today's state + the open-work queue | hard cap (~100 lines); nothing evergreen; finished work leaves the same day |
| the rulings ledger | dated decisions, newest first: the call, **why**, and what it supersedes — plus an OPEN list of undecided questions at the top | settled means settled: no session re-derives or relitigates a dated ruling |
| the glossary | the project's shared vocabulary, term by term | look a term up before coining a new one |
| `docs/` | evergreen reference — anything still true next month | one file per subject; the map points at each |
| the history | the narrative record: what happened, when, and why | where finished work from the handoff goes to rest |

The startup read is the map + the handoff + the OPEN list, capped together at a few hundred lines. Everything else is reached by pointer, on demand.

The rulings ledger is the highest-leverage file in the set, and the one existing repos most often lack: without it every session re-derives old decisions, and sometimes decides differently. It is also where dead alternatives live — "we tried that, and here is why it lost" is the expensive half of the knowledge, and it is exactly what a plain TODO list or commit history fails to carry.

## The reorganization — how to get an existing repo there

Run it as one deliberate pass, in this order. Nothing is deleted during the pass — facts move, everything else becomes a pointer or gets a status header.

1. **Inventory every doc surface.** All markdown in the repo (root files, `docs/`, `notes/`, scattered READMEs, TODO/NOTES/PLAN files), plus instruction files (`CLAUDE.md`, `AGENTS.md`, `.cursor/rules`, and the like), plus any wiki or long-lived issue text agents are expected to read. For each: what kinds of facts does it hold, and when did each part last get updated?
2. **Stand up the ledger set** — create whichever of the seven files don't exist yet, empty except for their charter line. The map's where-a-fact-goes table is written now, because every later step consults it.
3. **Classify and move, one surface at a time.** Each fact in the inventory is one of: map-fact, agent law, today-state, decision, term, evergreen reference, history, or **dead**. Move it to its home; leave a pointer behind if the old location still gets read. Highest-traffic surfaces first — the bloated root files are where the payoff is.
4. **Resolve duplicates — don't average them.** When two copies of a fact disagree, determine which is true (git history, the code itself, or the person who knows), put the true one in the home file, and turn the other into a pointer. A merge that keeps both phrasings keeps the contradiction.
5. **Mark the dead.** An executed or abandoned plan gets a `DONE` / `SUPERSEDED` header stating what happened and where the outcome lives — the text below it stays, in past tense from the header on down. Live-voice text about dead work misroutes every later reader; it is the single most common fault in an aged repo.
6. **Shrink the instruction files.** Root `CLAUDE.md` goes pointer-style: identity (what the product is, in a line), commands, invariants, pointers to everything else. Procedures move to skills. Rules that must hold move to hooks and are *removed* from prose — a rule stated in two registers drifts like any other duplicated fact. If the repo uses `AGENTS.md`, make `CLAUDE.md` an `@AGENTS.md` import or symlink; never maintain two copies.
7. **Commission the working subtrees.** Any directory agents repeatedly work in gets three things: a routing file (what's here, which child owns what — the mandatory first read), local law (a `CLAUDE.md` with only the rules that bind here), and a state file (which files here are canonical vs superseded, rewritten in place). Existing content in the subtree gets sorted canonical-or-superseded as part of this step — that sorting *is* the state file's first draft.
8. **Sweep.** Re-read every surviving surface against the new homes: stale claims, contradictions, dead pointers. This closing sweep is what turns a pile of moves into a consistent whole, and it re-runs at every future batch boundary — a subagent can do the whole sweep.

## Keeping it reorganized — freshness as a write discipline

The pass above decays immediately unless updates bind to the work instead of to a schedule:

- **Docs ride the work's own commit.** A fact your change invalidated is updated in its home file in the same commit, never "in a follow-up."
- **Dead plans get their header the day they die**, not at the next cleanup.
- **Finished work is evicted from the handoff** to the history file the day it finishes, leaving one line and a pointer.
- **The state file is rewritten as the last act of every pass that writes in its directory.** A stale state file misroutes every later agent, which costs more than the minute the update takes.

## Smells — when to run this

- The same fact in two files, disagreeing.
- A root `CLAUDE.md` past ~200 lines, or explaining the product in paragraphs instead of pointing.
- A session's first hour spent re-deriving a decision someone already made.
- Something in the handoff (or the "current status" section of any doc) that was true last month.
- A plan document in live voice for work that already shipped.
- A directory whose purpose you can only learn by opening its files.
- A "hard rule" that exists only as prose. Rules that must hold are hooks.
