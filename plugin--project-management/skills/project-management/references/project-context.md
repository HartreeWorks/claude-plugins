---
description: Show current project orientation and available documents
---

# /project-context

Display the current project's context, memory, and available documents. This is the manual version of what happens automatically on conversation start in a project folder.

## Prerequisites

Must be in a project folder (contains `project.yaml`).

## Flow

### Step 1: Verify project folder
Check that current directory contains `project.yaml`. If not, display error:
```
Error: Not in a project folder.
Run /list-projects to see available projects, or /new-project to create one.
```

### Step 2: Read project files
Read the following files:
- `project.yaml` - Get project name and type
- `CLAUDE.md` - Get About section
- `MEMORY.md` - Get Status, Where we are, What's next, and recent Log entries
- `TODO.md` - Get active tasks count and any urgent items
- `context/google-docs.yaml` - Get list of Google Docs
- List `context/` folder - Discover local files (excluding google-docs.yaml)

### Step 3: Display orientation

Present a natural summary based on the project state. The format should feel conversational, not like a rigid menu. Include:

1. **Project identity** - Name and what it's about
2. **Current state** - Status and where we are (from MEMORY.md)
3. **Active tasks** - Count and key items from TODO.md (if any)
4. **What's next** - Upcoming priorities or open questions
5. **Available resources** - Google Docs and local files (mention but don't enumerate in detail)
6. **Last session** - Brief note on what happened recently (if available)

### Formatting guidance

- Keep it concise - a few sentences, not a wall of text
- Mention key Google Docs by alias if they're marked as core
- Don't list every file - just note what's available
- If there's a handoff note from the last session, surface it
- End with an open prompt like "What would you like to work on?"

## Example output

```
This is the Website Redesign project - you're working on a complete refresh of HartreeWorks LTD's marketing site.

Currently in Phase 2 (Dec-Jan), focused on building the new component library with Alice and finalising the design system. Last session you reviewed the homepage wireframes with Bob.

You have 3 active tasks, including finalising the navigation structure and starting the responsive layouts.

I have access to the design-brief and meeting-notes docs, plus some local context files. What would you like to work on?
```
