#!/usr/bin/env python3
"""List all projects from the projects index.

Usage:
    python list_projects.py [--format table|simple|json]

Output formats:
    table  - Markdown table (default)
    simple - One project per line
    json   - JSON array
"""

import argparse
import json
import sys
from pathlib import Path

import yaml


PROJECTS_FILE = Path.home() / "Documents" / "Projects" / "projects.yaml"


def load_projects() -> list[dict]:
    """Load projects from the index file."""
    if not PROJECTS_FILE.exists():
        return []

    with open(PROJECTS_FILE) as f:
        data = yaml.safe_load(f)

    return data.get("projects", []) if data else []


def format_table(projects: list[dict]) -> str:
    """Format projects as a markdown table."""
    if not projects:
        return "No projects found."

    active = [p for p in projects if p.get("status") == "active"]
    archived = [p for p in projects if p.get("status") == "archived"]

    lines = ["| Project | Type | Status |", "|---------|------|--------|"]

    for p in active:
        lines.append(f"| {p.get('name', p.get('folder', 'Unnamed'))} | {p.get('type', '-')} | active |")

    for p in archived:
        lines.append(f"| {p.get('name', p.get('folder', 'Unnamed'))} | {p.get('type', '-')} | archived |")

    lines.append("")
    lines.append(f"**{len(active)} active**, {len(archived)} archived")

    return "\n".join(lines)


def format_simple(projects: list[dict]) -> str:
    """Format projects as simple lines."""
    if not projects:
        return "No projects found."

    lines = []
    for p in projects:
        status = p.get("status", "unknown")
        name = p.get("name", p.get("folder", "Unnamed"))
        ptype = p.get("type", "-")
        lines.append(f"{name} ({ptype}, {status})")

    return "\n".join(lines)


def format_json(projects: list[dict]) -> str:
    """Format projects as JSON."""
    return json.dumps(projects, indent=2)


def main():
    parser = argparse.ArgumentParser(description="List Claude Code projects")
    parser.add_argument(
        "--format", "-f",
        choices=["table", "simple", "json"],
        default="table",
        help="Output format (default: table)"
    )
    args = parser.parse_args()

    projects = load_projects()

    if args.format == "table":
        print(format_table(projects))
    elif args.format == "simple":
        print(format_simple(projects))
    elif args.format == "json":
        print(format_json(projects))


if __name__ == "__main__":
    main()
