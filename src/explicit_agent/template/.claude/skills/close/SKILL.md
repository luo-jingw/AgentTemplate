---
name: close
description: Reconcile implementation, project state, documentation, validation evidence, and reporting at task or phase closure.
---

# Trigger

Use at task or phase closure.

# Inputs

Read:
- current code diff;
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

Mark completed work accurately.

Do not mark blocked or unverified work as complete.

## Issues

Close resolved issues.

Record newly observed unresolved problems.

## Opportunities

Record future improvements that are not part of the current plan.

Do not promote them automatically.

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
- plan;
- issues;
- opportunities;
- docs.

Explicitly report anything not verified.
