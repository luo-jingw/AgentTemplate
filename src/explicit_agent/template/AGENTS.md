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
- `Plan Status`: `proposed → approved → completed`.
- Each phase's `Phase Status`:
  - `pending → active`;
  - `active → completed`;
  - `active → blocked`;
  - `blocked → active`, once the blocker is resolved;
  - `blocked → (return to plan)`, if the blocker invalidates the plan.
- At most one phase is `active`. A `blocked` phase blocks every later
  `pending` phase from becoming `active` until it is resolved. Zero
  phases are `active` while the plan is `proposed` or `completed`, or
  while the only unresolved phase is `blocked`.

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

## Content Boundary for Persistent Documents

A persistent document records facts, design, interfaces, constraints,
rationale, and open questions within its own scope. It does not record
how the user asked for it to be written.

Write for a reader who was not in the conversation. The document must
stand on its own and describe the current result directly.

Do not record:
- how the user phrased a request, e.g. "the user asked for...", "per
  the user's comment...";
- the writing process itself, e.g. "for discussion with
  collaborators", "not elaborated here", "avoid over-engineering
  here";
- any of the above wrapped in parentheses, a blockquote, a preamble, a
  footnote, or a side note.

When a correction changes a concept or a piece of logic, update the
affected text directly. Do not keep a trace of the conversation, such
as "previously understood as..." or "now changed to...". Record
decision history only where a log is explicitly required.

A constraint that only governs the writer's behavior is followed, not
written down. A constraint the system itself must satisfy is written
down as the constraint, its scope, and the expected behavior — not as
an instruction to the writer.

Parentheses are for terminology, units, formula conditions, or
citations only. Do not use them to smuggle in a writing instruction.

Before writing a sentence, check it: does it describe the subject
itself, or does it explain how a request was carried out? Delete the
latter.

| Do not write | Instead |
|---|---|
| "initial framework (not elaborating implementation here)" | "initial framework", matched to the actual level of detail |
| "for discussion with collaborators, to be revised" | delete |
| "observability (not visual similarity)" | define directly: "how available the information an action needs is in the model's input" |
| "do not modify raw data" as a note to the writer | if it is a system constraint: "raw data is read-only; processed results are written to a separate version" |

## Template Ownership

Every file copied from the `explicit-agent` template is either
template-owned or project-owned. Never both.

Template-owned (defined by the template, not by this project):
- `AGENTS.md`;
- the default skills: `.claude/skills/{plan,work,experiment,close}/SKILL.md`;
- `templates/module.md`;
- `templates/pr.md`;
- `docs/README.md`.

Project-owned (accumulates project-specific content) splits further by
whether the template ships a skeleton for it:

- Template-seeded — the template ships a starting version, so a
  template update can compare against it: `PROJECT.md`, `plan.md`,
  `issues.md`, `opportunities.md`.
- Project-created — nothing in the template corresponds to it; it
  exists only because this project made it: every file under `docs/`
  other than `docs/README.md`, and every project-specific skill under
  `.claude/skills/` not listed under Template-owned above.

Ownership (template-owned vs. project-owned) and update eligibility
(template-seeded vs. project-created) are different questions. A file
can be project-owned without having any template skeleton to sync
against.

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
  or merge it. Re-check on every future update — do not treat one
  reported conflict as a lasting decision to stop syncing that file.
- If the current template introduces a template-owned file whose path
  does not exist in the project, add it.
- If the current template introduces a template-owned file whose path
  already exists in the project as a project-owned file (for example, a
  project-specific skill later promoted to a default skill under the
  same name), stop and report the ownership conflict. Do not add it.

### Project-owned files

Never replace the content of a project-owned file.

Project-created files (see Template Ownership) have no template
skeleton to sync against. Never touch them during a template update —
not even the append step below.

Template-seeded project-owned files are either single-instance
(`PROJECT.md`, `plan.md`) or record-oriented (a file holding zero or
more repeated blocks with the same heading names — `issues.md` and
`opportunities.md`, each record starting with its own `# ISSUE-NNN` /
`# OPT-NNN` heading). A heading only identifies a unique location in a
single-instance file. Handle each kind differently.

**Single-instance files** — change only through the following two steps,
in order:

1. **Apply pending migrations.** Read the template's `migrations.json`.
   Apply every entry with an `id` greater than the "Last applied
   migration id" recorded in `PROJECT.md`, in order, to the file it
   names. An entry's `path` is the list of headings from the document
   root down to the target heading, so `# Structure` → `## Modules` and
   `# Code Mapping` → `## Modules` can be told apart:
   - `rename_section`: if the project's file has a heading at `path`,
     rename that heading (only) to `to`. Keep all content under it
     unchanged.
   - `delete_section`: if the project's file has a heading at `path`
     and its content still matches the entry's `expected_blank`
     placeholder, delete the section. If the content differs, do not
     delete it — stop and report that the section is deprecated and
     needs a manual decision.
2. **Append new sections.** Compare the file's current heading paths
   against the current template's, path by path. For each path present
   in the template but missing from the project's file: if its parent
   path already exists in the project's file, insert it, with the
   template's placeholder content, as the last child under that parent.
   If it has no parent (a top-level heading), append it at the end of
   the file. Do not reorder or touch existing headings.

**Record-oriented files** — do not run migrations or the append step on
them. A heading like `## Evidence` repeats once per record, so neither a
`path` nor a plain heading name identifies a single occurrence, and an
automatic append cannot tell which record a new field belongs to. A
change to the per-record schema (e.g. adding a field every future
`ISSUE-NNN` should have) is a breaking template change: call it out
explicitly instead of encoding it as a migration, and apply it by hand
per project.

After finishing, update `PROJECT.md`'s "Last synced to" and "Last
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

This list is exhaustive for ordinary implementation and planning work.
Completing a phase, a task, or a work unit is not a stop condition by
itself. A specific procedure in this file (for example, Template
Updates) may define additional stop conditions scoped to its own
workflow; those apply on top of this list, not instead of it.

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
