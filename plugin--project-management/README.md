# Project Management Plugin

Manage non-coding projects with scaffolding, Google Docs integration, and memory tracking.

## Installation

1. Add the HartreeWorks plugins marketplace:
```
/plugin marketplace add hartreeworks/claude-plugins
```

2. Install this plugin:
```
/plugin install project-management@hartreeworks-plugins
```

## Features

### Commands

| Command | Purpose |
|---------|---------|
| `/list-projects` | Show all projects with status |
| `/setup-project-switcher` | Set up shell `projects` command |

### Skill

The plugin includes the full **project-management** skill which provides:

- `/new-project` - Create a new project with scaffolding
- `/add-google-doc` - Add Google Doc to project
- `/create-doc` - Create new Google Doc via MCP
- `/project-context` - Display current project orientation
- `/tasks` - View and manage project tasks
- `/migrate-project` - Import from Claude.ai
- `/archive-project` - Move project to archive

## Quick start

### 1. List your projects

```
/list-projects
```

### 2. Set up the shell switcher (optional)

Run `/setup-project-switcher` to add the `projects` command to your shell. This lets you quickly navigate to project directories:

```bash
$ projects

  1. Plans and Reviews
  2. Client Project

  a all  q quit
```

Press a number to cd into that project and launch Claude.

### 3. Create a new project

```
/new-project
```

You'll be asked for:
1. Project name
2. Type (client / personal / planning)
3. Brief description
4. Initial focus

Projects are created in `~/Documents/Projects/`.

## Project structure

Each project folder contains:

```
project-folder/
├── project.yaml     # Project metadata
├── CLAUDE.md        # About, conventions, instructions
├── MEMORY.md        # Dynamic context tracking
├── TODO.md          # Task tracking
├── context/         # Reference materials
├── work/            # Active work and outputs
└── assets/          # Images, data files
```

## Requirements

- Python 3.9+
- PyYAML (`pip install pyyaml`)

For Google Docs integration:
- Google Workspace MCP server configured
