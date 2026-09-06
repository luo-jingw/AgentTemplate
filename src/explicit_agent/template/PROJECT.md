# PROJECT.md

Project-specific context that supplements `AGENTS.md`.

`AGENTS.md` is fixed across projects.
`PROJECT.md` accumulates what is specific to this one.

Update this file when a new project-specific constraint, environment
detail, or convention is discovered during work.

Do not duplicate:
- verified architecture → `docs/`;
- current work → `plan.md`;
- unresolved problems → `issues.md`.

## Template

- Initialized from (source, version, or commit):
- Last synced to (source, version, or commit):
- Last applied migration id (see the template's `migrations.json`):

## Purpose

What this project is for and who it serves.

## Environment

- Platform / hardware:
- Shared with (other users or projects on the same account or machine):
- Constraints imposed by the environment:

## Credentials

Services that require a scoped identity in this project (git remotes,
package registries, model hubs, cloud APIs).

| Service | Scope | Source | Notes |
|---|---|---|---|

Do not assume a global or default identity applies.
See `AGENTS.md` → Credentials and Environment Isolation.

Do not record token values or other secrets here.

## Project-Specific Constraints

Rules that apply only to this project, in addition to `AGENTS.md`.

## Onboarding

What a new contributor must read or know before making the first change.
