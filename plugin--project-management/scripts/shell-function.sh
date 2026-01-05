# Add this to your .zshrc or .bashrc:

projects() {
    local dir
    dir=$(python3 ~/.claude/skills/project-management/scripts/projects_selector.py)
    if [ -n "$dir" ] && [ -d "$dir" ]; then
        cd "$dir"
    fi
}
