# Phase I Spec: Todo In-Memory Python Console App

## Objective
Build a CLI-based todo application that stores tasks in memory.

## Functional Requirements
1. **Add Task**: Input title and optional description.
2. **Delete Task**: Remove a task using its unique ID.
3. **Update Task**: Modify existing task details (title, description).
4. **View Task List**: Display all tasks in a formatted table (using `rich`).
5. **Mark as Complete**: Toggle the completion status of a task.

## Technical Requirements
- **Runtime**: Python 3.13+
- **Dependency Management**: `uv`
- **Output Formatting**: `rich` library for tabular data and colors.
- **Pattern**: Simple MVC-like structure (Models, Terminal UI Controller).
- **Storage**: In-memory list of objects.

## Data Model
```python
class Todo:
    id: int
    title: str
    description: str
    is_completed: bool
```

## CLI Interface Commands
- `add "Title" "Description"`
- `list`
- `done <id>`
- `update <id> --title "New Title"`
- `delete <id>`
- `exit`
