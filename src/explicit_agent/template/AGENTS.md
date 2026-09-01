# AGENTS.md

## Core Principle

Everything is explicit.

## Project Structure

- One file has one responsibility.
- File names express their responsibility.
- Do not place unrelated classes in one file.
- Do not place large groups of peer-level functions in one file.
- Related functions belong to a class or a dedicated submodule.

## Dependencies

- Declare every dependency explicitly through import or include.
- Do not use wildcard imports.
- Do not use dynamic imports.
- Do not use global variables for hidden communication between modules.
- Every C++ source file includes its direct dependencies.
- Do not rely on transitive includes.

## Interfaces

- Separate interface from implementation.
- C++ uses `.h` and `.cpp` separation.
- Python `__init__.py` contains exports only.
- Critical Python module boundaries use `Protocol` or `ABC`.
- Every function parameter and return value has an explicit type.
- Structured data uses `dataclass`, `TypedDict`, or an explicit class.
- Do not use bare dictionaries as interfaces.

Avoid:
- metaclass-generated APIs;
- `__getattr__` proxy APIs;
- decorators that modify public signatures;
- complex macros that generate public interfaces.

If a dynamic mechanism is unavoidable, provide an explicit static interface beside it.

## Design

Use this order without reordering:

Problem
→ Structure
→ Interface
→ Flow
→ Code Mapping
→ Tasks

Rules:

- Define module boundaries before implementation.
- Every critical state has exactly one owner.
- Other modules read the state or modify it through an explicit interface.
- Prefer stable interfaces over implementation convenience.
- Each task changes one module or one mechanism.
- Each task has an explicit observation or validation method.
- Every module, interface, state, and task maps to concrete files.

## Implementation

- Implement only the minimum required mechanism.
- Do not add fallback designs.
- Do not add redundant designs.
- Do not redesign unrelated modules while implementing a task.

If the current plan is invalid:

STOP
→ update the problem
→ return to `plan`

Do not redesign in place.

## Validation

Prefer observational validation.

Expose measured values directly, including:
- latency;
- numerical error;
- shape;
- dtype;
- memory usage;
- allocation count;
- kernel count;
- checksums.

Do not encode expected performance values as pass/fail assertions unless explicitly required.

## Persistent State

`plan.md`
- Current approved work.
- Structure, interfaces, flows, files, and implementation phases.

`issues.md`
- Observed unresolved problems.
- Evidence, hypotheses, and next experiments.

`opportunities.md`
- Possible future improvements.
- Not part of the current plan unless explicitly promoted.

`docs/`
- The repository's verified world model.
- Current architecture.
- Current interfaces.
- Measured results.
- Verified decisions.

Do not store unresolved hypotheses in `docs/`.

## Skills

Default skills live in `.claude/skills/`:
- `plan`
- `work`
- `close`

Do not create a new skill for:
- project state;
- one-off tasks;
- facts;
- temporary implementation details;
- unresolved hypotheses.

When the same workflow or user correction repeats across multiple tasks, report it at closure as a possible skill candidate.

Do not create or modify a project skill without explicit approval.

## Project-Specific Skills

Project-specific skills may be created from:

- repeated workflows observed in this project;
- explicit user requirements;
- external reference skills or engineering procedures.

External skills are references, not specifications.

When adapting an external skill:

1. Read the current project rules and relevant source files first.
2. Extract the reusable workflow and constraints.
3. Remove repository-specific names, paths, tools, and assumptions that do
   not apply.
4. Map every procedure to the current project's modules, commands, and
   persistent state.
5. Preserve useful stop conditions and acceptance criteria only when they
   are valid for this project.
6. Generate a new project-owned skill under `.claude/skills/`.

Do not copy an external skill verbatim unless explicitly requested.

Do not modify the base template repository.

When creating a project-specific skill, report before writing the file:
- source concepts kept;
- source concepts removed;
- project-specific additions.

## Stop Conditions

Stop and report the blocker when:
- state ownership is ambiguous;
- a required interface is undefined;
- required evidence is unavailable;
- implementation requires crossing an undeclared module boundary;
- the implementation no longer matches the approved plan;
- a required dependency or environment is unavailable.

Do not guess through a stop condition.

## Git Attribution

Git history represents project contributors and technical changes.

Do not include agent, model, assistant, or tool attribution in:

- commit messages;
- commit trailers;
- branch names;
- tags;
- pull request titles;
- pull request descriptions generated for this repository.

Do not add entries such as:

- `Co-authored-by: Claude ...`
- `Co-authored-by: ChatGPT ...`
- `Co-authored-by: Codex ...`
- `Generated-by: ...`
- `Assisted-by: ...`

Do not mention the use of an AI agent unless the user explicitly requests it.

Commit messages describe:
- what changed;
- why it changed.

They do not describe which tool produced the change.

Do not modify:
- `user.name`;
- `user.email`;
- commit author;
- commit committer identity.

Use the repository user's existing Git identity.
If no Git identity is configured, stop and report it.
Do not invent an identity.

## Git Push

Do not rewrite authorship or attribution before pushing.

Do not amend commits solely to add agent attribution.

Do not add agent attribution to satisfy tool-generated defaults.

Push only the commits intended for the current task.
