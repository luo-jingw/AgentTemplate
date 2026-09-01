"""Copy the explicit-agent template into the current working directory."""

from __future__ import annotations

import shutil
import sys
from pathlib import Path
from typing import List

TEMPLATE_ROOT = Path(__file__).resolve().parent / "template"


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


def copy_template(destination: Path, template_root: Path) -> List[Path]:
    copied: List[Path] = []
    for source in iter_template_files(template_root):
        relative = source.relative_to(template_root)
        target = destination / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, target)
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
