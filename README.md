# explicit-agent

Minimal explicit agent development scaffold.

## Scope

This project hands a new project three things: a set of working
conventions (`AGENTS.md`), a minimal skill vocabulary (`plan`, `work`,
`experiment`, `close`), and a handful of blank persistent-state files.
That is the whole product.

It does not run inside a project, enforce its conventions, or validate
a project's state at runtime. After initialization, the copied files
belong to the project — how strictly they get followed, how ambiguity
gets resolved, how the project grows its own skills, is up to the
agent working in that project, not this tool. See the copied
`AGENTS.md` for those conventions; this README and `CONTRIBUTING.md`
are about the template itself, not about how to run a project.

This tool does not update, sync, merge, or repair an existing project — bringing a project up to date with a newer template is a manual, agent-assisted procedure, defined in the copied `AGENTS.md` under "Template Ownership" and "Template Updates".

## Use

Run `explicit-agent-init` in an empty or non-conflicting project directory.

From GitHub:

```bash
uvx \
  --from git+https://github.com/luo-jingw/AgentTemplate.git \
  explicit-agent-init
```

After cloning this repository:

```bash
git clone https://github.com/luo-jingw/AgentTemplate.git
cd <project-dir>
uvx --from <path-to>/AgentTemplate explicit-agent-init
```

If any destination file already exists, the command changes nothing and prints the conflicting paths.

## Copied files

```text
AGENTS.md
PROJECT.md
plan.md
issues.md
opportunities.md
docs/README.md
.claude/skills/plan/SKILL.md
.claude/skills/work/SKILL.md
.claude/skills/experiment/SKILL.md
.claude/skills/close/SKILL.md
templates/module.md
templates/pr.md
```

Project-specific skills may be added under `.claude/skills/`. They stay in the project. They are not copied back to this repository.

## Previewing the output

`src/explicit_agent/template/` is copied verbatim — read it there to see what `explicit-agent-init` produces without running the command.
