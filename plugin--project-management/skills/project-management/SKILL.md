---
name: project-management
description: This skill should be used when the user says "new project", "create project", "add google doc", "list projects", "show projects", "migrate project", "archive project", "project context", "project help", or mentions managing non-coding projects, client projects, personal projects, planning projects, Google Docs integration, or project memory. Handles project scaffolding, document management, and project lifecycle.
---

# Project Management

Manage non-coding projects (client work, personal projects, planning) with full scaffolding, Google Docs integration, and memory tracking.

## Overview

Projects are stored in `~/Documents/Projects/` with:
- `projects.yaml` - Central index of all projects
- `projects.code-workspace` - VS Code/Cursor workspace for easy access

Each project folder contains:

- `project.yaml` - Project metadata
- `CLAUDE.md` - About, conventions, instructions
- `MEMORY.md` - Dynamic context tracking
- `TODO.md` - Task tracking
- `.gitignore` - Sensible defaults for Git
- `context/` - Reference materials for Claude to understand
  - `google-docs.yaml` - Google Docs manifest (local files just go directly in context/)
- `work/` - Active work (drafts, outputs, deliverables)
- `assets/` - Images, data files, attachments
- `.claude/archive/` - Archived memories (auto-managed)

### Folder purposes

| Folder | Purpose | Examples |
|--------|---------|----------|
| `context/` | Reference materials you want Claude to know about | Client briefs, specs, research, examples, brand guidelines |
| `work/` | Where the actual work happens | Drafts, iterations, completed outputs |
| `assets/` | Supporting files that aren't documents | Images, data files, screenshots, recordings |
| `.claude/archive/` | Archived memory sessions (auto-managed) | Old session logs |

## Commands

| Command | Purpose |
|---------|---------|
| `/new-project` | Create a new project with scaffolding |
| `/add-google-doc` | Add Google Doc to project |
| `/create-doc` | Create new Google Doc via MCP |
| `/list-projects` | Show all projects with status (script-backed) |
| `/project-context` | Display current project orientation |
| `/tasks` | View and manage project tasks |
| `/migrate-project` | Import from Claude.ai |
| `/archive-project` | Move project to archive |
| `/project-help` | Show command reference |
| `/setup-project-switcher` | Set up shell `projects` command |

### Script-backed commands

Some commands have scripts for faster execution:

**`/list-projects`** - Run:
```bash
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/list_projects.py
```
Supports `--format table|simple|json`. Use `json` when other skills need to parse the output.

## Quick Start

### Creating a Project

Invoke `/new-project` and provide:
1. Project name
2. Type (client / personal / planning)
3. Brief description (for About section)
4. Initial focus (for memory)

The skill creates `~/Documents/Projects/YYYY-MM-{slug}/` with all files.

### Adding Documents

**Google Docs:** From within a project folder, invoke `/add-google-doc` with:
- A Google Docs/Sheets/Slides URL
- A search term to find docs in Drive

Each Google Doc gets an alias, purpose, and core flag.

**Local files:** Simply place them in the `context/` folder - no registration needed.

### Project Behaviour (Embedded in Each Project)

On conversation start in a project folder:
- Read MEMORY.md, TODO.md, context/google-docs.yaml, and list context/ folder
- Present a brief, natural orientation based on current project state
- Mention active task count if there are tasks

During conversation:
- Load relevant docs proactively when context suggests they'd help
- Update MEMORY.md when significant things happen
- Update TODO.md when tasks are completed or new tasks emerge
- When wrapping up, add a handoff note to the Log

## File Formats

### project.yaml

```yaml
name: "Project Name"
folder: "2025-09-project-name"
type: client  # client|personal|planning
created: 2025-09-15
skill_version: "1.0"
template: default
```

### context/google-docs.yaml

```yaml
docs:
  - name: "Document Title"
    alias: "short alias"
    type: google_doc  # google_doc|google_sheet|google_slides
    id: "abc123..."   # Google doc ID
    url: "https://..."
    purpose: "Brief description"
    core: true  # Show at conversation start
```

Note: Local files in `context/` don't need registration - Claude discovers them directly.

### MEMORY.md Structure

```markdown
# Project Memory

**Status:** Active - [current phase]

## Context
[Narrative background about the project - builds up over time]

## Where we are
- Current situation and focus

## What's next
- Upcoming priorities
- Open questions?

## Log
- **YYYY-MM-DD:** What happened, decisions made, handoff notes
```

### TODO.md Structure

```markdown
# Tasks

## Active
- [ ] Task description
- [ ] Another task

## Waiting
- [ ] Task blocked on something → reason/note

## Later
- [ ] Future consideration

## Done
- [x] 2024-12-30: Completed task
```

**Difference from MEMORY.md:**
- MEMORY.md's "What's next" = strategic direction (priorities, open questions)
- TODO.md = tactical tasks (concrete, checkable items)

### Central Index (~/Documents/Projects/projects.yaml)

```yaml
projects:
  - folder: "2025-09-project-name"
    name: "Project Name"
    type: client
    status: active  # active|archived
```

## Memory Management

Update MEMORY.md when significant things happen:
- Decisions are made
- Focus or priorities change
- Meaningful progress occurs
- Wrapping up a session (add a handoff note to the Log)

Keep the memory concise - summarise rather than accumulate. When the Log gets long, consolidate older entries or archive to `.claude/archive/`.

## Google Docs Integration

Fetch documents using MCP tools:
- `mcp__google-workspace__get_doc_content` for Google Docs
- `mcp__google-workspace__get_spreadsheet_info` + `read_sheet_values` for Sheets
- `mcp__google-workspace__get_presentation` for Slides
- `mcp__google-workspace__search_drive_files` to find docs by name

Extract doc ID from URLs using: `/d/([a-zA-Z0-9-_]+)/`

User email for MCP: `your-email@gmail.com`

## Folder Naming

Project folders use the format `YYYY-MM-{slug}`:
- YYYY-MM from project creation date (or original start date for migrations)
- slug: lowercase, hyphens, no special characters

Example: `2025-09-client-project`

## Archiving Projects

Invoke `/archive-project` to:
1. Update status to "archived" in projects.yaml
2. Move folder to `~/Documents/Projects/_archive/`

## Migrating from Claude.ai

Invoke `/migrate-project` to import existing Claude.ai projects:
1. Gather project name, type, and original start date
2. Paste Memory content from Claude.ai
3. Paste Instructions (optional)
4. Paste Google Doc URLs
5. Creates project with `migrated_from: claude_ai` flag

## Additional Resources

### Reference Files

For detailed command procedures, consult:

- **`references/new-project.md`** - Full /new-project flow with templates
- **`references/add-google-doc.md`** - Google Doc addition procedures
- **`references/migrate-project.md`** - Migration flow from Claude.ai
- **`references/create-doc.md`** - Creating new Google Docs
- **`references/archive-project.md`** - Archiving procedures

### Quick Reference

- **`references/project-context.md`** - Context display format
- **`references/list-projects.md`** - Project listing format
- **`references/tasks.md`** - Task management command
- **`references/project-help.md`** - Help command output
