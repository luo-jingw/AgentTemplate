---
name: experiment
description: Run a structured multi-variable investigation as a grid instead of one change at a time, and report results as a table.
---

# Trigger

Use when a task requires empirical comparison across multiple variables,
configurations, or parameters, rather than a single well-defined change.

Examples: performance tuning, hyperparameter sweeps, comparing
implementations, isolating which of several factors causes a result.

Do not use for a single targeted change with a known correct outcome —
use `work` directly.

# Inputs

Read:
- `AGENTS.md`;
- `PROJECT.md`;
- active phase in `plan.md`, if the experiment is part of approved work;
- relevant `issues.md`;
- relevant `docs/`;
- relevant source files.

# Preconditions

- The question being investigated is stated explicitly.
- The variables that plausibly affect the outcome are identifiable.

# Procedure

Use this order without reordering:

Research
→ Analysis
→ Experiment Grid
→ Run and Record
→ Result Analysis
→ Report

## Research

State what is already known or assumed about the variables and the
mechanism under test.

## Analysis

List the variables that plausibly affect the outcome.

For each variable, state the levels or values to test.

Identify variables to hold fixed and record their fixed value.

## Experiment Grid

Enumerate every cell to run before running any of them.

A cell changes only the variables under test; fixed variables stay
constant across all cells.

Do not run cells opportunistically. Define the grid first.

## Run and Record

Run every cell in the grid.

Record for each cell:
- the exact configuration;
- the command;
- the raw measured result;
- the environment.

Do not discard a cell's result because it looks wrong. Record it and flag
it.

## Result Analysis

Compare cells. Do not attribute a result to a variable that changed
together with another variable.

State which variables the evidence supports and which it does not.

## Report

Report all cells as one table, not as a narration of individual runs.

Table columns: variables under test, fixed variables (if not constant
across the whole grid), and the measured result.

State the conclusion and its confidence separately from the table.

# Stop Conditions

Stop when:
- the grid cannot be run under fixed conditions (for example, a shared or
  noisy environment invalidates comparison);
- a required measurement is unavailable.

If the grid is impractically large, reduce it explicitly and record why,
rather than reverting to one-at-a-time changes.

# Completion

An experiment ends with:
- the full grid and its results as one table;
- a stated conclusion and its confidence;
- verified conclusions moved to `docs/`;
- unresolved findings moved to `issues.md`;
- unexplored grid cells moved to `opportunities.md`, if relevant.
