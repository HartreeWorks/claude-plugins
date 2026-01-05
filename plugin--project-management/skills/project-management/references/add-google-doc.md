---
description: Add a Google Doc to the current project
---

# /add-google-doc

Add an existing Google Doc, Sheet, or Slides to the current project's context/google-docs.yaml manifest.

For local files, simply place them in the `context/` folder - no registration needed.

## Prerequisites

Must be in a project folder (contains `project.yaml`).

## Flow

### Step 1: Verify project folder
Check that current directory contains `project.yaml`. If not, display error:
```
Error: Not in a project folder.
Run /list-projects to see available projects, or /new-project to create one.
```

### Step 2: Get document reference
Ask the user: "What would you like to add? You can provide:
- A Google Doc/Sheet/Slides URL
- A search term to find a Google Doc"

### Step 3: Process based on input type

**If Google Doc URL:**
1. Extract doc ID using regex: `/d/([a-zA-Z0-9-_]+)/`
2. Determine doc type from URL:
   - `docs.google.com/document` → google_doc
   - `docs.google.com/spreadsheets` → google_sheet
   - `docs.google.com/presentation` → google_slides
3. Fetch document title using appropriate MCP tool:
   - For docs: `mcp__google-workspace__get_doc_content` (extract title)
   - For sheets: `mcp__google-workspace__get_spreadsheet_info`
   - For slides: `mcp__google-workspace__get_presentation`

**If search term:**
1. Search Google Drive using `mcp__google-workspace__search_drive_files`
2. Display results and ask user to confirm which document
3. Extract doc ID and type from selected result

### Step 4: Check for duplicates
Read `context/google-docs.yaml` and check if doc ID already exists.
If duplicate found, ask: "This document is already in the project. Update its entry? (yes/no)"

### Step 5: Gather metadata
Ask the user:
- "Short alias for this doc? (e.g., 'project sheet', 'notes')"
- "Brief description of its purpose?"
- "Is this a core doc that should be mentioned at conversation start? (yes/no)"

### Step 6: Add to context/google-docs.yaml
Read current `context/google-docs.yaml`, add new entry:

```yaml
- name: "{document title}"
  alias: "{user's alias}"
  type: {google_doc|google_sheet|google_slides}
  id: "{extracted doc ID}"
  url: "{original URL}"
  purpose: "{user's description}"
  core: {true|false}
```

### Step 7: Confirm
Display:
```
Added to project:
  Name: {name}
  Alias: {alias}
  Type: {type}
  Core: {yes/no}

Use "read the {alias}" to load this document in conversation.
```

## Arguments

The skill can accept an optional argument:
- `/add-google-doc https://docs.google.com/...` - Add directly from URL

If argument provided, skip Step 2 and proceed with that input.

## Error Handling

- **Invalid URL:** "Could not parse Google Doc URL. Please check the URL format."
- **Doc not found:** "Could not access this document. Check permissions or try searching by name."
- **MCP auth error:** "Google authentication required. The auth flow should start automatically."
