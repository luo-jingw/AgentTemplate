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

`PROJECT.md`
- Project-specific context that supplements this file.
- Environment, credentials, constraints, onboarding notes.
- Update when a new project-specific fact is discovered.

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

## Template Ownership

Every file copied from the `explicit-agent` template is either
template-owned or project-owned. Never both.

Template-owned (defined by the template, not by this project):
- `AGENTS.md`;
- the default skills: `.claude/skills/{plan,work,experiment,close}/SKILL.md`;
- `templates/module.md`;
- `templates/pr.md`;
- `docs/README.md`.

Project-owned (accumulates project-specific content):
- `PROJECT.md`;
- `plan.md`;
- `issues.md`;
- `opportunities.md`;
- every file under `docs/` other than `docs/README.md`;
- every project-specific skill under `.claude/skills/` not listed above.

Do not hand-edit a template-owned file to record project-specific
content. Record it in `PROJECT.md`, `docs/`, `issues.md`, or
`opportunities.md` instead, per their ownership above.

Do not delete a heading the template put in a project-owned file, even
if unused. Leave it blank instead. A future template update may need to
find it.

## Template Updates

The template evolves independently of any project built from it. A
project may fall behind the template it was initialized from.

When asked to bring a project up to date with a newer template:

### Template-owned files

- For each template-owned file, compare the project's copy against the
  version it was initialized from (or last synced to), recorded in
  `PROJECT.md`. If that record is missing, ask before proceeding.
- If the project's copy is unchanged, replace it with the current
  template version.
- If the project's copy was hand-edited despite the ownership rule,
  stop and report the conflict for that file. Do not silently overwrite
  or merge it. From then on, that file's sync is the project's own
  responsibility.
- If the current template introduces a template-owned file the project
  does not have, add it.

### Project-owned files

Never replace the content of a project-owned file. Only change it
through the following two steps, in order.

1. **Apply pending migrations.** Read the template's `migrations.json`.
   Apply every entry with an `id` greater than the "Last applied
   migration id" recorded in `PROJECT.md`, in order, to the file it
   names:
   - `rename_section`: if the project's file has the `from` heading,
     rename it to `to`. Keep all content under it unchanged.
   - `delete_section`: if the project's file has this heading and its
     content still matches the entry's `expected_blank` placeholder,
     delete the section. If the content differs, do not delete it —
     stop and report that the section is deprecated and needs a manual
     decision.
2. **Append new sections.** For each project-owned file, compare its
   current headings against the current template's headings for that
   file. Append any heading present in the template but missing from
   the project's file, with the template's placeholder content, to the
   end of the file. Do not reorder or touch existing headings.

After both steps, update `PROJECT.md`'s "Last synced to" and "Last
applied migration id" to the current values.

## Skills

Default skills live in `.claude/skills/`:
- `plan`
- `work`
- `experiment`
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
- a required dependency or environment is unavailable;
- a credential or environment identity is missing or ambiguous.

This list is exhaustive. Completing a phase, a task, or a work unit is not
a stop condition by itself.

Once a plan is approved, continue executing its remaining phases without
pausing for confirmation between them.

Record a non-blocking observation in `issues.md` and continue. Do not stop
work to report it. Surface accumulated issues at the next `close`, or when
the user returns.

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

## Credentials and Environment Isolation

Do not assume a global or default identity, token, or account applies to
this project.

Applies to git remotes, package registries, model hubs, cloud CLIs, and
any other credential-scoped service.

Before using a credential:
- Check for a project-scoped or repository-scoped configuration first.
- If the project runs on a shared account or shared machine, do not use
  the global default identity or token.
- If scope is ambiguous or a required credential is missing, stop and ask
  the user. Do not guess, reuse another user's credential, or fall back to
  a global default.

Record the resolved scope and source of each credential in `PROJECT.md`.
Do not record token values or other secrets in any persistent file.
