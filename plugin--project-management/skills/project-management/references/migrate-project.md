---
description: Import a project from Claude.ai into the Claude Code project system
---

# /migrate-project

Import an existing Claude.ai project into the Claude Code project system by copying over memory, instructions, and document references.

## Flow

### Step 1: Gather basic info
Ask the user:
- "What's the project name?"
- "What type of project? (client / personal / planning)"
- "When was this project started? (YYYY-MM format, e.g., 2025-09)"

### Step 2: Generate folder name
Create folder name as `{YYYY-MM}-{slug}` where:
- YYYY-MM is from user input (original project start date)
- slug is the project name converted to lowercase, spaces replaced with hyphens

### Step 3: Create folder structure
Create `~/Documents/Projects/{folder-name}/` with:
- `project.yaml`
- `CLAUDE.md`
- `MEMORY.md`
- `context/` subfolder (with google-docs.yaml inside)
- `work/` subfolder
- `assets/` subfolder
- `.claude/archive/` subfolder

### Step 4: Import Memory
Ask: "Please paste the Memory section from your Claude.ai project (the text from the Memory panel):"

Parse the pasted content and use it to populate:
- `MEMORY.md` Context section (the narrative background)
- Extract any "current focus" type content for "Where we are" section

### Step 5: Import Instructions
Ask: "Please paste the Instructions from your Claude.ai project (or say 'skip' if none):"

If provided, add to CLAUDE.md Instructions section.

### Step 6: Get About summary
Ask: "What's a brief About summary for this project? (This describes what the project is)"

Use for CLAUDE.md About section.

### Step 7: Get Conventions
Ask: "Any conventions to note? (spelling, terminology, formatting - or say 'skip')"

If provided, add to CLAUDE.md Conventions section.

### Step 8: Import Documents
Ask: "Paste Google Doc URLs from your Claude.ai project, one per line (or say 'done' when finished):"

For each URL:
1. Extract doc ID using regex: `/d/([a-zA-Z0-9-_]+)/`
2. Fetch document title using MCP
3. Ask: "Alias for '{title}'?"
4. Ask: "Purpose? (brief description)"
5. Ask: "Core doc? (yes/no)"
6. Add to context/google-docs.yaml

Continue until user says 'done'.

### Step 9: Populate files

**project.yaml:**
```yaml
name: "{project name}"
folder: "{YYYY-MM-slug}"
type: {client|personal|planning}
created: {YYYY-MM-DD from user input}
skill_version: "1.0"
template: default
migrated_from: claude_ai
migrated_on: {current YYYY-MM-DD}
```

**CLAUDE.md:** (with all sections populated from above)

**MEMORY.md:** (with imported memory content)

**context/google-docs.yaml:** (with all imported docs)

### Step 10: Update central index
Add entry to `~/Documents/Projects/projects.yaml`

### Step 11: Initialize git
Run `git init` in the project folder.

### Step 12: Confirm
Display:
```
Migration complete: {project name}
Location: ~/Documents/Projects/{YYYY-MM-slug}/

Imported:
- Memory content
- {N} documents
- Instructions and conventions

Next steps:
- cd ~/Documents/Projects/{YYYY-MM-slug}
- Review CLAUDE.md and MEMORY.md
- Start a conversation to test the setup
```

## Tips for users

Before running this skill, in Claude.ai:
1. Open your project
2. Click the Memory section and copy the full text
3. Click the Instructions section (if you have one) and copy it
4. Note the URLs of any Google Docs in the Files section

## Error handling

- **Invalid URL during doc import:** Skip that URL and continue with others
- **MCP auth error:** Prompt user to complete auth, then continue
- **Duplicate project folder:** Ask if user wants to overwrite or use a different name
