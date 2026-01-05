---
description: Create a new Google Doc and add it to the current project
---

# /create-doc

Create a new Google Doc via Google Workspace MCP and add it to the project's context/google-docs.yaml.

## Prerequisites

Must be in a project folder (contains `project.yaml`).

## Flow

### Step 1: Verify project folder
Check that current directory contains `project.yaml`. If not, display error:
```
Error: Not in a project folder.
Run /list-projects to see available projects, or /new-project to create one.
```

### Step 2: Get document details
Ask the user:
- "What should the document be called?"
- "Brief description of its purpose?"

### Step 3: Check for initial content
Ask: "Any initial content to add? (paste content, or say 'empty' for a blank doc)"

### Step 4: Create Google Doc
Use `mcp__google-workspace__create_doc` with:
- `user_google_email`: "pete.hartree@gmail.com"
- `title`: {document name from Step 2}
- `content`: {initial content if provided}

Capture the returned document ID and URL.

### Step 5: Gather remaining metadata
Ask the user:
- "Short alias for this doc? (e.g., 'notes', 'draft')"
- "Is this a core doc that should be mentioned at conversation start? (yes/no)"

### Step 6: Add to context/google-docs.yaml
Read current `context/google-docs.yaml`, add new entry:
```yaml
- name: "{document title}"
  alias: "{user's alias}"
  type: google_doc
  id: "{doc ID from creation}"
  url: "{doc URL from creation}"
  purpose: "{user's description}"
  core: {true|false}
```

### Step 7: Confirm
Display:
```
Created and added to project:
  Name: {name}
  Alias: {alias}
  URL: {url}
  Core: {yes/no}

Open in browser: {url}
Use "read the {alias}" to load this document in conversation.
```

## Arguments

The skill can accept an optional argument for the document name:
- `/create-doc Meeting Notes` - Create doc with that title, then prompt for other details

## Error Handling

- **MCP auth error:** "Google authentication required. The auth flow should start automatically."
- **Creation failed:** "Failed to create document. Error: {error message}"
- **google-docs.yaml write error:** "Document created but failed to add to context/google-docs.yaml. Doc URL: {url}"
