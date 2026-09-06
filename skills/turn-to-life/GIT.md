# Git is the change protocol

Read before editing a Git working tree or changing Git state, including single-agent work.
Git preserves inspectable versions and change boundaries; it does not establish correctness
or authorize publication. Project policy and explicit user instructions govern this default.

## 1. Establish the baseline and ownership

Confirm the actual repository root, current branch/HEAD, working-tree status, staged changes,
and any in-progress merge/rebase/cherry-pick. Inspect relevant diffs, including untracked
files reported by status; do not infer ownership from who last committed a file.

A small read-only starting point is:

```sh
git rev-parse --show-toplevel
git status --short --branch
git diff --stat
git diff --cached --stat
```

Read the applicable project instructions, branch/PR policy, ignore rules, and relevant hooks
before writes. Record only decision-changing baseline facts in the existing plan or brief.
Do not capture unrelated source or secrets in a new status log. If another operation is
in progress, do not continue or abort it without establishing ownership and authority.

Existing staged, unstaged, untracked, and ignored work belongs to its owner. Preserve its
content and staging state. Do not stash, reset, clean, switch branches, or commit it merely
to obtain a clean tree. Stop the affected operation when ownership cannot be separated;
independent safe work may continue. Uncommitted or ignored data is not safely backed up
merely because the directory contains `.git`.

If Git is absent, follow the project's version-control policy. Initialize only the intended
project root when authorized project creation includes that setup; otherwise clarify before
initializing or changing version-control systems. Never initialize a parent/home directory,
create a remote, choose public visibility, or invent an author identity as a convenience.

## 2. Choose enough isolation

Follow the existing branch policy. A small, single-owner change may stay on the current
branch when permitted; a branch per edit is not a goal. Use a named task branch/worktree
when concurrent writing, uncertain experiments, existing user work, or project policy needs it.
Verify its path, starting commit, and branch before writing; carry them in the existing brief.

Writing agents use the isolation rules in [SUBAGENTS.md](SUBAGENTS.md). Never let concurrent
agents mutate one shared Git index or branch; disjoint file paths alone do not isolate Git
operations. A worktree provides a separate working directory and index, not a security
sandbox or independent remotes. Coordinate shared refs and repository-wide Git operations.
Worktrees start from committed state; required uncommitted inputs are not carried over.
Establish a safe, scoped source for missing inputs rather than silently using stale code.
Gitignored inputs need a separately scoped, safe path; do not copy an entire private workspace.

## 3. Make coherent, reviewable commits

Default to local commits of coherent, owned changes unless the user/project requests a
patch-only workflow or another commit policy. Do not ask again for routine commits covered
by that policy. Keep the implementation, relevant tests, and its necessary contract/routing
updates together. One commit should explain one meaningful change, not one tool call.

Before committing, verify the retained scope through the current quality/stage rules.
Review the exact staged diff and its full file list for unintended content, secrets, local
artifacts, and license obligations. Stage owned paths or reviewed hunks, not blanket changes;
`git add -A` is appropriate only when the entire affected set is owned and has been reviewed.
Pre-existing staged changes are especially important: adding only your path does not exclude
someone else's already-staged content from an ordinary commit. Use verified isolation or
resolve ownership first; do not silently unstage their work.

Respect hooks, signing, and project-required checks. Do not bypass failures or alter global
Git configuration to get a commit through. Write an informative message explaining the
change; preserve material rationale, verification evidence, and limits in its body or the
existing task record. Inspect the resulting commit and status, including changes made by hooks.

A labeled exploratory checkpoint may preserve unfinished work with known gaps. It is not
a verified delivery or release. Do not weaken checks to disguise it as one. If required
commit checks prevent a checkpoint, retain recoverable files and report the limitation.
A clean tree is not worth deleting useful work, and a commit hash is not proof of quality.

## 4. Integrate deliberately; recover without collateral damage

The integration owner reviews the exact contribution and base, resolves shared contracts,
and follows the project's merge strategy. When remote state matters, fetch and inspect
divergence before selecting an integration action; do not blindly pull into unknown state.
A conflict-free merge still needs the affected composition checks. Conflicts are a content
and ownership decision, not permission to choose an entire side automatically.

Prefer a new corrective commit for shared/published history. Amend, rebase, reset, force-push,
or destructive clean-up require authority for the affected history/content and a verified
recovery path; they are never automatic remedies for a rejected push or dirty tree.
Do not discard changes with reset/restore/checkout/clean or remove branches/worktrees until
ownership and actual recoverability are established. Remove task worktrees only after their
useful output is integrated or explicitly preserved and no active worker depends on them.

## 5. Separate local completion from publication

A local commit, remote push, PR, release/tag, and deployment are different state changes.
Perform each only when the user or an existing scoped project policy authorizes it. Carry
valid approval forward; do not ask for every push it already covers. Editing permission
alone is not publication permission. Check whether a push triggers deployment or other effects.

Before publishing, confirm the destination repository, visibility, branch/ref, exact commits,
and applicable checks. Inspect the whole outgoing range—not only the last commit—for private
material or unrelated changes. Do not create/change remotes, visibility, credentials, or
protection rules implicitly. On rejection, inspect the cause; do not automatically force.
After publishing, verify the remote ref and any claimed live result. Report queued or failed
CI/deployments honestly rather than equating an accepted push with a successful release.

Finish with the relevant commit(s), verification, local versus published state, and remaining
owned or pre-existing changes. A user's unrelated dirty files may remain. Never manufacture
repository-wide cleanliness to satisfy a completion phrase. If Git actions are unavailable
or prohibited, return the patch/artifact locations and the specific unmet Git step instead.

For command semantics, consult the matching installed Git documentation or the on-demand
[reference shelf](REFERENCES.md); this protocol chooses workflow policy, not new Git behavior.
