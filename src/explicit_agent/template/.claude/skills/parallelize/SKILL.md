---
name: parallelize
description: Execute two or more independent phases from an approved plan concurrently, each in its own git worktree and subagent, then merge them back in order.
---

# Trigger

Use when the active round in `plan.md` holds two or more phases with no
unmet dependency and no overlapping modified files.

Do not use for a single phase, or when phases in the round share a
modified file — those run sequentially through `work` instead, in
dependency order.

# Inputs

Read:
- `AGENTS.md`;
- `PROJECT.md`;
- the active round's phases in `plan.md`;
- relevant `issues.md`.

# Preconditions

- `plan.md` has `Plan Status: approved`.
- The project is a git repository with a clean working tree.
- Every phase in the round is `Phase Status: pending`, its dependencies
  are all `completed`, and its modified files do not overlap another
  phase in the same round.

If any of these does not hold, do not proceed — run the round's phases
through `work` instead.

# Procedure

1. For each phase in the round, create a git worktree on its own
   branch, named for the phase (e.g. `phase-2`), and set its
   `Phase Status: active`.
2. Dispatch one subagent per phase, scoped to that phase's worktree, to
   run `work` for that phase only.
3. Wait for every subagent to finish or report a blocker.
4. Merge each completed phase's branch into the integration branch, in
   phase-number order. Do not merge a phase that reported a blocker;
   set its `Phase Status: blocked` instead, with the blocker recorded
   in `issues.md`.
5. If a merge conflicts, stop and report it. Do not resolve it by
   discarding either side without inspecting it.
6. Remove each merged phase's worktree.

# Stop Conditions

Stop when:
- a merge conflicts;
- a subagent reports a blocker;
- the working tree is not clean before starting;
- a phase's modified files turn out to overlap another phase's in the
  same round, once work is underway.

# Completion

A parallel round ends with:
- every phase in the round `completed`, `blocked`, or reported as an
  unresolved merge conflict;
- the integration branch containing every successfully merged phase;
- no leftover worktrees;
- updated persistent state, same as `work`'s Completion.

If a later round's dependencies are now all `completed`, it becomes the
next active round — through `parallelize` again if it qualifies, or
through `work` otherwise.
