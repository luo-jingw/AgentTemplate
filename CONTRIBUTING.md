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
project-specific content that an update must not destroy. Changes to
their skeleton are constrained:

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

## Adding a migration entry

Append an entry to `src/explicit_agent/migrations.json`. Do not edit or
remove past entries — the list is append-only history.

```json
{
  "id": "0001",
  "file": "PROJECT.md",
  "op": "rename_section",
  "from": "## Old Heading",
  "to": "## New Heading"
}
```

```json
{
  "id": "0002",
  "file": "PROJECT.md",
  "op": "delete_section",
  "heading": "## Old Heading",
  "expected_blank": "<the exact placeholder text this heading previously carried>"
}
```

Rules:
- `id` is a zero-padded, monotonically increasing string across the
  whole file, regardless of which project-owned file the entry targets.
- `file` is the path relative to a project's root.
- `expected_blank` must be the exact placeholder text the section held
  before deletion, taken from the template version immediately prior to
  this change. It is what lets an update tell an untouched section
  apart from one a project already filled in.
- Only `rename_section` and `delete_section` exist. Do not invent a new
  operation without updating both this file's schema and the "Template
  Updates" algorithm in the copied `AGENTS.md`.
