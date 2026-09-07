"""Copy the explicit-agent template into the current working directory."""

from __future__ import annotations

import json
import shutil
import subprocess
import sys
from importlib import metadata
from pathlib import Path
from typing import List, Optional

TEMPLATE_ROOT = Path(__file__).resolve().parent / "template"
MIGRATIONS_FILE = Path(__file__).resolve().parent / "migrations.json"
PROJECT_FILE = Path("PROJECT.md")


def iter_template_files(root: Path) -> List[Path]:
    files: List[Path] = []
    stack: List[Path] = [root]
    while stack:
        current = stack.pop()
        for entry in current.iterdir():
            if entry.is_dir():
                stack.append(entry)
            elif entry.is_file():
                files.append(entry)
    files.sort()
    return files


def find_conflicts(destination: Path, template_root: Path) -> List[Path]:
    conflicts: List[Path] = []
    for source in iter_template_files(template_root):
        relative = source.relative_to(template_root)
        if (destination / relative).exists():
            conflicts.append(relative)
    return conflicts


def _package_version() -> str:
    try:
        return metadata.version("explicit-agent")
    except metadata.PackageNotFoundError:
        return "unknown"


def _git_commit(path: Path) -> Optional[str]:
    try:
        result = subprocess.run(
            ["git", "rev-parse", "--short", "HEAD"],
            cwd=path,
            capture_output=True,
            text=True,
            timeout=2,
        )
    except (OSError, subprocess.TimeoutExpired):
        return None
    if result.returncode != 0:
        return None
    return result.stdout.strip() or None


def _vcs_commit_from_install_metadata() -> Optional[str]:
    # When installed from a VCS URL (e.g. `uvx --from git+https://...`),
    # PEP 610 has pip/uv record the exact commit in direct_url.json. This
    # is the only case TEMPLATE_ROOT itself won't be inside a .git
    # worktree, so it is the one worth covering explicitly.
    try:
        raw = metadata.distribution("explicit-agent").read_text("direct_url.json")
    except metadata.PackageNotFoundError:
        return None
    if not raw:
        return None
    try:
        commit = json.loads(raw).get("vcs_info", {}).get("commit_id")
    except ValueError:
        return None
    return commit[:12] if commit else None


def _template_source_label(template_root: Path) -> str:
    version = _package_version()
    commit = _vcs_commit_from_install_metadata() or _git_commit(template_root)
    if commit:
        return f"explicit-agent {version} ({commit})"
    return f"explicit-agent {version}"


def _latest_migration_id() -> str:
    try:
        entries = json.loads(MIGRATIONS_FILE.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return "0"
    if not entries:
        return "0"
    return max(entries, key=lambda entry: int(entry["id"]))["id"]


def _fill_project_provenance(target: Path, template_root: Path) -> None:
    source_label = _template_source_label(template_root)
    replacements = {
        "- Initialized from (source, version, or commit):":
            f"- Initialized from (source, version, or commit): {source_label}",
        "- Last synced to (source, version, or commit):":
            f"- Last synced to (source, version, or commit): {source_label}",
        "- Last applied migration id (see the template's `migrations.json`):":
            "- Last applied migration id (see the template's `migrations.json`): "
            + _latest_migration_id(),
    }
    text = target.read_text(encoding="utf-8")
    for old, new in replacements.items():
        text = text.replace(old, new)
    target.write_text(text, encoding="utf-8")


def copy_template(destination: Path, template_root: Path) -> List[Path]:
    copied: List[Path] = []
    for source in iter_template_files(template_root):
        relative = source.relative_to(template_root)
        target = destination / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, target)
        if relative == PROJECT_FILE:
            _fill_project_provenance(target, template_root)
        copied.append(relative)
    return copied


def main() -> None:
    if len(sys.argv) != 1:
        sys.stderr.write("usage: explicit-agent-init\n")
        raise SystemExit(2)

    if not TEMPLATE_ROOT.is_dir():
        sys.stderr.write("explicit-agent template directory is missing\n")
        raise SystemExit(2)

    destination = Path.cwd()
    conflicts = find_conflicts(destination, TEMPLATE_ROOT)
    if conflicts:
        sys.stderr.write("conflict: existing files, no files modified\n")
        for relative in conflicts:
            sys.stderr.write(f"{relative.as_posix()}\n")
        raise SystemExit(1)

    copied = copy_template(destination, TEMPLATE_ROOT)
    for relative in copied:
        sys.stdout.write(f"{relative.as_posix()}\n")
    raise SystemExit(0)
