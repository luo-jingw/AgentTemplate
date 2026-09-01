---
name: work
description: Execute an approved plan, investigate unexpected behavior, and perform controlled implementation or optimization work.
---

# Trigger

Use when executing an approved phase from `plan.md`.

# Inputs

Read:
- `AGENTS.md`;
- active phase in `plan.md`;
- relevant source files;
- relevant docs;
- related open issues.

# Preconditions

- An approved active phase exists in `plan.md`.
- Affected modules, files, interfaces, and state ownership are defined.
- Affected source files can be inspected.

# Procedure

1. Confirm the active phase.
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
- required evidence is unavailable.

Do not silently redesign the system.

# Completion

A work unit ends with:
- code state;
- observed result;
- updated persistent state;
- explicit remaining blocker, if any.
