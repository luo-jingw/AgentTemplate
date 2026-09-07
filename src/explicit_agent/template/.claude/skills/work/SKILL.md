---
name: work
description: Execute an approved plan, investigate unexpected behavior, and perform controlled implementation or optimization work.
---

# Trigger

Use when:
- executing an approved phase from `plan.md`; or
- making a trivial, local change that does not meet any `plan` trigger
  condition (no new subsystem, no architecture/cross-module/interface/
  ownership change, no complex performance work).

# Inputs

Read:
- `AGENTS.md`;
- `PROJECT.md`;
- active phase in `plan.md`;
- relevant source files;
- relevant docs;
- related open issues.

# Preconditions

For planned work:
- `plan.md` has `Plan Status: approved`.
- Exactly one phase has `Phase Status: active`, or one `pending` phase can
  be set to `active` to start it.
- Affected modules, files, interfaces, and state ownership are defined.
- Affected source files can be inspected.

For direct work (no plan):
- The change is local: it does not require a new interface, a state
  ownership change, or crossing an undeclared module boundary.
- The observation or validation method is explicit before changing code.
- Affected source files can be inspected.

If a direct change turns out to need an interface, ownership, or module
boundary change, stop and route it to `plan` instead of continuing.

# Procedure

1. Confirm the active phase, or confirm the change is in scope for direct
   work. If a phase is `pending`, set it to `Phase Status: active`.
2. Confirm affected modules and files.
3. Confirm interfaces and state ownership.
4. Measure current behavior when relevant.
5. Make the minimum required change.
6. Change one mechanism at a time where practical.
7. Run targeted observational validation.
8. Record measured results.
9. Update persistent state.

# Investigation

Separate:

Observation
→ Evidence
→ Hypothesis
→ Experiment
→ Conclusion

Do not state a hypothesis as fact.

# Performance Work

Separate:
- end-to-end latency;
- subsystem latency;
- kernel execution;
- launch and synchronization overhead;
- copy and layout conversion;
- CPU gaps.

Do not attribute a result when multiple variables changed simultaneously.

When the question spans multiple variables or configurations, use the
`experiment` skill instead of iterating one change at a time.

# Continuity

After a plan is approved, execute its phases continuously.

Do not stop between phases to ask for confirmation. A completed phase is
not a stop condition. When a phase finishes, set its `Phase Status` to
`completed`, set the next `pending` phase to `active`, and continue. If
no `pending` phase remains, set `Plan Status: completed`.

If a phase cannot proceed, set its `Phase Status` to `blocked` and
follow the Stop Conditions below rather than leaving its status
ambiguous.

When a non-blocking issue appears, record it in `issues.md` and continue.
Do not pause work to report it.

# State Updates

Verified fact:
→ `docs/`

Unresolved problem:
→ `issues.md`

Future improvement:
→ `opportunities.md`

Approved work change:
→ return to `plan`

# Stop Conditions

Stop when:
- the plan assumption is invalid;
- an interface must change unexpectedly;
- state ownership must change;
- work crosses the declared module boundary;
- required evidence is unavailable;
- a credential or environment identity is missing or ambiguous.

This list is exhaustive for phase execution, on top of the global stop
conditions in `AGENTS.md`. Do not stop merely because a phase completed.

Do not silently redesign the system.

# Completion

A work unit ends with:
- code state;
- observed result;
- updated persistent state;
- explicit remaining blocker, if any.
