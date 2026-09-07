# Contributing to explicit-agent

This file is not copied into initialized projects. It constrains how
this template itself may change, so that a project built from an older
version of the template can be updated safely and mechanically. The
update procedure a project follows is defined in
`src/explicit_agent/template/AGENTS.md` under "Template Updates".

## File classes

`src/explicit_agent/template/` files are either template-owned or
project-owned, per the definitions in the copied `AGENTS.md`
("Template Ownership"). The rules below depend on which class a change
touches.

## Template-owned files

Template-owned files (`AGENTS.md`, the default skills, `templates/*.md`,
`docs/README.md`) are replaced wholesale in an unmodified project on
update. Any change to them is safe to make — there is no partial
structure to preserve. No migration entry is needed.

## Project-owned files

Project-owned files (`PROJECT.md`, `plan.md`, `issues.md`,
`opportunities.md`, non-README files under `docs/`) accumulate
project-specific content that an update must not destroy. They split
into two kinds, handled differently:

- **Single-instance** (`PROJECT.md`, `plan.md`, a given `docs/` file):
  one document, so a heading names a unique location — the tree of
  headings from the document root down to a given heading is stable.
- **Record-oriented** (`issues.md`, `opportunities.md`): zero or more
  repeated blocks with the same heading names, each block starting
  with its own `# ISSUE-NNN` / `# OPT-NNN` heading. A heading like
  `## Evidence` occurs once per record, so no heading path identifies
  a single occurrence across the whole file.

### Single-instance files

**Always allowed, no migration entry needed:**
- Adding a new heading (`#`/`##`/`###`) that did not exist before.

**Requires a `migrations.json` entry:**
- Renaming an existing heading.
- Deleting an existing heading.

**Not supported by the update mechanism — avoid, or call out explicitly
in the pull request / commit description as a breaking change:**
- Reordering, merging, or splitting existing headings.
- Rewriting the placeholder text under an existing heading in a way
  that changes its meaning (rewording for clarity is fine; changing
  what the section is asking for is not).

### Record-oriented files

No migration entry can target one record — a project may have any
number of `ISSUE-NNN` / `OPT-NNN` blocks, unknown to the template in
advance, and a `path` naming a heading inside one record does not
generalize to the others. Do not write a `migrations.json` entry for
these files.

A change to the per-record schema (e.g. every future `ISSUE-NNN`
should also have a `## Reproduction` field) is a breaking template
change with no automatic update path. Call it out explicitly in the
pull request / commit description; existing projects apply it by hand,
per record, if they choose to.

## Adding a migration entry

Append an entry to `src/explicit_agent/migrations.json`. Do not edit or
remove past entries — the list is append-only history. Only for
single-instance files (see above).

`path` is the list of headings from the document root down to the
target heading, in order — for example `["# Structure", "## Modules"]`
distinguishes that heading from the unrelated `## Modules` under
`# Code Mapping` in the same file.

```json
{
  "id": "0001",
  "file": "PROJECT.md",
  "op": "rename_section",
  "path": ["## Old Heading"],
  "to": "## New Heading"
}
```

```json
{
  "id": "0002",
  "file": "PROJECT.md",
  "op": "delete_section",
  "path": ["## Old Heading"],
  "expected_blank": "<the exact placeholder text this heading previously carried>"
}
```

Rules:
- `id` is a zero-padded, monotonically increasing string across the
  whole file, regardless of which project-owned file the entry targets.
- `file` is the path relative to a project's root, and must name a
  single-instance file.
- `path` entries are heading text exactly as it appears in the
  template (including the `#` markers), from the document root down to
  the target heading.
- `expected_blank` must be the exact placeholder text the section held
  before deletion, taken from the template version immediately prior to
  this change. It is what lets an update tell an untouched section
  apart from one a project already filled in.
- Only `rename_section` and `delete_section` exist. Do not invent a new
  operation without updating both this file's schema and the "Template
  Updates" algorithm in the copied `AGENTS.md`.
