---
name: plan
description: Converge a non-trivial change from problem definition to executable implementation phases.
---

# Trigger

Use this skill for:
- new subsystems;
- architecture changes;
- cross-module changes;
- interface changes;
- state ownership changes;
- complex performance work.

# Inputs

Read:
- `AGENTS.md`;
- `PROJECT.md`;
- current `plan.md`;
- relevant `issues.md`;
- relevant `opportunities.md`;
- relevant `docs/`;
- affected source files.

# Preconditions

- Affected source files can be inspected.
- Required facts for structure, ownership, and interfaces can be obtained from the repository.

# Procedure

Use this order without reordering:

Problem
→ Structure
→ Interface
→ Flow
→ Code Mapping
→ Implementation Phases

## Problem

Define:
- current observable state;
- exact problem;
- measurable goal.

Check every constraint already recorded in `PROJECT.md`, `issues.md`,
or `plan.md` against this goal (see `AGENTS.md` → Constraint
Provenance). Do not inherit a narrower scope than the goal requires
merely because a constraint already exists.

## Structure

Define:
- modules;
- responsibility of each module;
- ownership of every critical state.

Do not discuss implementation before module boundaries are explicit.

## Interface

Define:
- function or class interfaces;
- inputs;
- outputs;
- state transitions.

Interfaces must map to concrete files.

## Flow

Describe runtime execution using explicit objects and interfaces.

Avoid implicit references.

## Code Mapping

Map:
- module → file;
- interface → file;
- state → owner file;
- task → modified files.

A plan without complete file mapping is incomplete.

For each phase, derive its dependencies from this mapping: phase B
depends on phase A if B reads or modifies a file or state that A
creates or changes. Two phases with no dependency between them and no
overlapping modified files are independent.

## Implementation Phases

Each phase contains:
- `Phase Status: pending`;
- `Round`: its position in the dependency order (see below);
- goal;
- modified files;
- new structures;
- affected modules;
- dependencies (other phases that must complete first), if any;
- observation method.

Each phase changes one module or one mechanism where practical.

Group phases into rounds: round 1 holds every phase with no
dependency; each later round holds phases whose dependencies are all in
an earlier round. If no such grouping exists because two phases depend
on each other, stop — the dependency has a cycle and the plan is not
executable as structured.

Phases in the same round with disjoint modified files are independent
and may run through `parallelize`. Phases that share a modified file,
even within the same round, run sequentially through `work` instead.

# Stop Conditions

Stop planning when:
- required facts are unknown;
- ownership cannot be assigned uniquely;
- an interface cannot be stated explicitly;
- required source code has not been inspected;
- a persisted constraint narrows scope in a way inconsistent with, or
  not yet checked against, the current top-level goal;
- phase dependencies form a cycle.

Record the blocker in `issues.md`.

# Completion

Planning is complete only when:

problem_defined
→ structure_defined
→ ownership_defined
→ interfaces_defined
→ flows_defined
→ files_mapped
→ phases_observable
→ plan_closed

When the user approves the plan, set `Plan Status: approved` in `plan.md`
before starting `work`.
