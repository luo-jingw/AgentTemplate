---
name: close
description: Reconcile implementation, project state, documentation, validation evidence, and reporting at task or phase closure.
---

# Trigger

Use at task or phase closure.

# Inputs

Read:
- current code diff;
- `PROJECT.md`;
- `plan.md`;
- `issues.md`;
- `opportunities.md`;
- affected `docs/`;
- validation outputs.

# Preconditions

- The work being closed has a code state.
- Persistent project files can be inspected.

# Procedure

## Code

Verify:
- file responsibility;
- dependency explicitness;
- interface consistency;
- state ownership.

## Plan

Mark completed work accurately: set each finished phase's
`Phase Status: completed`. If every phase is `completed`, set
`Plan Status: completed`.

Do not mark blocked or unverified work as complete. Set `Phase Status:
blocked` instead, with the blocker recorded in `issues.md`.

If the project is under git version control and `Plan Status` is now
`completed`, commit `plan.md` in its completed state, then reset it to
the blank template for the next plan (see `AGENTS.md` → History
Retention). If the project is not under git version control, leave the
completed plan in place.

## Issues

Close resolved issues: if the project is under git version control,
remove the resolved entry from `issues.md` — git history preserves it.
If it is not, set `Status: Resolved` and keep the entry.

Record newly observed unresolved problems.

## Opportunities

Record future improvements that are not part of the current plan.

Do not promote them automatically.

Once an opportunity is promoted into a plan or explicitly rejected: if
the project is under git version control, remove its entry from
`opportunities.md`; if not, set its `Status` and keep it.

## Docs

Update only verified facts.

Remove or correct facts invalidated by the implementation.

## Validation

Record:
- what was observed;
- environment;
- command;
- raw result where useful;
- what was not observed.

## Skill Candidate

Check whether the completed work exposed a repeated reusable workflow.

Report a candidate only when:
- the procedure has repeated;
- the procedure is stable;
- forgetting it would create meaningful cost;
- it is a workflow rather than project state or fact.

Report format:

```text
Skill candidate: <name>

Reason:
The same workflow has appeared repeatedly.
```

Do not create the skill.

# Completion

Closure requires consistency between:
- code;
- `PROJECT.md`;
- plan;
- issues;
- opportunities;
- docs.

Explicitly report anything not verified.
