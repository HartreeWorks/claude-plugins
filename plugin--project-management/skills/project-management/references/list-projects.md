---
description: Show all projects from the central index
---

# /list-projects

Display all projects from `~/Documents/Projects/projects.yaml`.

## Implementation

Run the script:

```bash
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/list_projects.py
```

### Output formats

The script supports different formats via `--format`:

| Format | Use case |
|--------|----------|
| `table` | Default. Markdown table for human reading |
| `simple` | One line per project, good for quick lists |
| `json` | Machine-readable, for other skills to parse |

Examples:
```bash
# Default table output
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/list_projects.py

# Simple format
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/list_projects.py --format simple

# JSON for programmatic use
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/list_projects.py --format json
```

## For other skills

If another skill needs to know what projects exist, call the script with `--format json` and parse the output.
