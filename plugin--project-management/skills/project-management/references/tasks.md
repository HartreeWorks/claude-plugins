---
description: View and manage project tasks
---

# /tasks

Quick task management for the current project. Works alongside organic TODO.md updates that happen during conversation.

## Prerequisites

Must be in a project folder (contains `project.yaml` and `TODO.md`).

## Usage

### View tasks
```
/tasks
```

Shows:
- Active task count
- Waiting task count (with any that have been waiting too long)
- List of active tasks

### Add a task
```
/tasks add Write the project proposal
```

Adds to the Active section.

### Complete a task
```
/tasks done 2
```

Marks the 2nd active task as complete, moves it to Done with today's date.

### Move to waiting
```
/tasks wait 1 Waiting on feedback from Max
```

Moves task 1 to Waiting section with note.

### Move to later
```
/tasks later 3
```

Moves task 3 to Later section.

## Flow

### Viewing tasks

1. Read `TODO.md`
2. Parse sections (Active, Waiting, Later, Done)
3. Display summary:

```
📋 Tasks for {project name}

Active (3):
1. [ ] Schedule co-working call with Fin
2. [ ] Add podcast transcription skill
3. [ ] Write up grader requirements

Waiting (1):
⏳ Feedback from Max on budget → waiting since 2024-12-29

Later: 2 items
Done: 4 recent completions
```

### Adding tasks

1. Parse the task text after `add`
2. Append to Active section: `- [ ] {task text}`
3. Confirm: "Added: {task text}"

### Completing tasks

1. Find the nth task in Active section
2. Mark as `[x]` with date
3. Move to Done section: `- [x] {YYYY-MM-DD}: {task text}`
4. Confirm: "Completed: {task text}"

### Moving to waiting

1. Find the nth task in Active section
2. Move to Waiting section with note: `- [ ] {task text} → {note}`
3. Confirm: "Moved to waiting: {task text}"

### Moving to later

1. Find the nth task in Active section
2. Move to Later section
3. Confirm: "Moved to later: {task text}"

## TODO.md format

The skill expects this structure:

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

## Organic behaviour

Beyond the `/tasks` command, Claude also:

- **On conversation start:** Reads TODO.md, mentions active task count
- **During work:** Marks tasks complete when done, offers to add new tasks as they emerge
- **On session end:** Ensures completed work is reflected in TODO.md
- **Maintenance:** Clears old Done items when the section exceeds ~10 entries
