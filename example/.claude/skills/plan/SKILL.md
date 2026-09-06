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

## Implementation Phases

Each phase contains:
- goal;
- modified files;
- new structures;
- affected modules;
- observation method.

Each phase changes one module or one mechanism where practical.

# Stop Conditions

Stop planning when:
- required facts are unknown;
- ownership cannot be assigned uniquely;
- an interface cannot be stated explicitly;
- required source code has not been inspected.

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
