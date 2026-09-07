"""Copy the explicit-agent template into the current working directory."""

from __future__ import annotations

import shutil
import subprocess
import sys
from importlib import metadata
from pathlib import Path
from typing import List, Optional

TEMPLATE_ROOT = Path(__file__).resolve().parent / "template"
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


def _template_source_label(template_root: Path) -> str:
    version = _package_version()
    commit = _git_commit(template_root)
    if commit:
        return f"explicit-agent {version} ({commit})"
    return f"explicit-agent {version}"


def _fill_project_provenance(target: Path, template_root: Path) -> None:
    source_label = _template_source_label(template_root)
    replacements = {
        "- Initialized from (source, version, or commit):":
            f"- Initialized from (source, version, or commit): {source_label}",
        "- Last synced to (source, version, or commit):":
            f"- Last synced to (source, version, or commit): {source_label}",
        "- Last applied migration id (see the template's `migrations.json`):":
            "- Last applied migration id (see the template's `migrations.json`): 0",
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
