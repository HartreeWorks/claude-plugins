---
description: Set up the projects shell function for quick directory switching
allowed-tools: Bash(grep:*), Bash(cat:*), Bash(realpath:*), Read, Edit, AskUserQuestion
---

# Setup project switcher

Set up the `projects` shell function for quick project navigation from the terminal.

## Workflow

### Step 1: Check current status

Check if the function already exists:

```bash
grep -q "^projects()" ~/.zshrc 2>/dev/null && echo "EXISTS_ZSHRC" || (grep -q "^projects()" ~/.bashrc 2>/dev/null && echo "EXISTS_BASHRC" || echo "NOT_FOUND")
```

### Step 2: Get plugin path

Resolve the plugin installation path:

```bash
realpath ${CLAUDE_PLUGIN_ROOT}
```

### Step 3: Handle based on status

**If already exists:**
- Tell the user the function is already configured
- Offer to show current configuration or update it

**If not found:**

1. Generate the shell function using the resolved plugin path:

```
# Project switcher (added by project-management plugin)
projects() {
    local dir
    dir=$(python3 {RESOLVED_PATH}/scripts/projects_selector.py)
    if [ -n "$dir" ] && [ -d "$dir" ]; then
        cd "$dir" && claude
    fi
}
```

2. Ask the user using AskUserQuestion:
   - Header: "Shell config"
   - Question: "Add the projects() function to your shell configuration?"
   - Options:
     - label: "Add to ~/.zshrc"
       description: "For zsh users (default on macOS)"
     - label: "Add to ~/.bashrc"
       description: "For bash users"
     - label: "Show function only"
       description: "Display so you can add it manually"

3. If user chooses to add:
   - Read the shell config file
   - Append a blank line, comment, and the function
   - Use the Edit tool to append to the file
   - Tell user to run `source ~/.zshrc` or open a new terminal

4. If user chooses "Show function only":
   - Display the function
   - Tell them to add it to their shell config manually

### Step 4: Confirm

Tell the user:
```
Done! To activate now, run: source ~/.zshrc

Usage: Type `projects` in your terminal to see your projects and quickly navigate to one.
```
