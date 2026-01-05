#!/usr/bin/env python3
"""Interactive project selector for shell integration.

Displays numbered list of projects, returns selected path to stdout.
Shell function captures output and runs cd.

Usage: Called by shell function, not directly.
"""

import sys
import tty
import termios
from pathlib import Path

import yaml


def getch() -> str:
    """Read a single character from stdin without waiting for Enter."""
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


PROJECTS_DIR = Path.home() / "Documents" / "Projects"
PROJECTS_FILE = PROJECTS_DIR / "projects.yaml"


def load_projects() -> list[dict]:
    """Load projects from the index file."""
    if not PROJECTS_FILE.exists():
        return []

    with open(PROJECTS_FILE) as f:
        data = yaml.safe_load(f)

    return data.get("projects", []) if data else []


def display_projects(projects: list[dict], show_all: bool = False) -> list[dict]:
    """Display numbered project list, return displayed projects."""
    # Filter and sort (most recent first - reverse alpha on folder works due to YYYY-MM prefix)
    if show_all:
        filtered = sorted(projects, key=lambda p: p.get("folder", ""), reverse=True)
    else:
        filtered = sorted(
            [p for p in projects if p.get("status") == "active"],
            key=lambda p: p.get("folder", ""),
            reverse=True
        )

    if not filtered:
        print("No projects found.", file=sys.stderr)
        return []

    # Display
    print(file=sys.stderr)
    for i, p in enumerate(filtered, 1):
        name = p.get("name", p.get("folder", "Unnamed"))
        status = "" if p.get("status") == "active" else " (archived)"
        print(f"  {i}. {name}{status}", file=sys.stderr)

    print(file=sys.stderr)

    # Footer hint
    archived_count = len([p for p in projects if p.get("status") == "archived"])
    if show_all or archived_count == 0:
        print("  q quit", file=sys.stderr)
    else:
        print(f"  a all ({archived_count} archived)  q quit", file=sys.stderr)

    print(file=sys.stderr)
    return filtered


def main():
    projects = load_projects()
    if not projects:
        print("No projects found.", file=sys.stderr)
        sys.exit(1)

    show_all = False
    displayed = display_projects(projects, show_all)

    while True:
        try:
            ch = getch()
        except (EOFError, KeyboardInterrupt):
            print(file=sys.stderr)
            sys.exit(0)

        # Handle Ctrl+C and Ctrl+D
        if ch in ('\x03', '\x04'):
            print(file=sys.stderr)
            sys.exit(0)

        choice = ch.lower()

        if choice == "q":
            print(file=sys.stderr)
            sys.exit(0)

        if choice == "a" and not show_all:
            show_all = True
            displayed = display_projects(projects, show_all)
            continue

        try:
            idx = int(choice)
            if 1 <= idx <= len(displayed):
                folder = displayed[idx - 1].get("folder", "")
                name = displayed[idx - 1].get("name", folder)
                path = PROJECTS_DIR / folder
                if path.exists():
                    print(f"\n  Opening {name}...\n", file=sys.stderr)
                    print(path)  # This goes to stdout for the shell function
                    sys.exit(0)
                else:
                    print(f"Directory not found: {path}", file=sys.stderr)
            else:
                print(f" (1-{len(displayed)})", file=sys.stderr)
        except ValueError:
            pass  # Ignore invalid keys silently


if __name__ == "__main__":
    main()
