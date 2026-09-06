# explicit-agent

Minimal explicit agent development scaffold.

After initialization, the copied files belong to the project. This tool does not update, sync, merge, or repair an existing project — bringing a project up to date with a newer template is a manual, agent-assisted procedure, defined in the copied `AGENTS.md` under "Template Ownership" and "Template Updates".

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

## Example

`src/explicit_agent/template/` is copied verbatim — read it there to see what `explicit-agent-init` produces without running the command.
