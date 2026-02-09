# Evolution of Todo - Phase I

A simple, in-memory console todo application built with Python. Manage your tasks directly from the terminal with a menu-driven interface.

## Features

- **Add Tasks** - Create new tasks with descriptions
- **View Tasks** - See all tasks with completion status
- **Update Tasks** - Modify task descriptions
- **Delete Tasks** - Remove completed or unwanted tasks
- **Mark Complete/Incomplete** - Track your progress

## Quick Start

### Prerequisites

- Python 3.11 or higher
- No external dependencies (standard library only)

### Running the Application

```bash
python todo.py
```

### First Time Usage

```
=== Todo Application ===

--- Menu ---
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Mark Complete
6. Mark Incomplete
7. Exit
Enter choice (1-7):
```

## User Guide

### Menu Options

| Option | Description |
|--------|-------------|
| `1. Add Task` | Create a new task |
| `2. View Tasks` | Display all tasks with status |
| `3. Update Task` | Modify an existing task |
| `4. Delete Task` | Remove a task |
| `5. Mark Complete` | Mark task as done |
| `6. Mark Incomplete` | Mark task as not done |
| `7. Exit` | Close the application |

### Adding a Task

1. Select `1` from the menu
2. Enter your task description
3. Press Enter

```
Enter choice (1-7): 1
Enter task description: Buy groceries
Task added (ID: 1)
```

### Viewing Tasks

Select `2` to see all your tasks:

```
Enter choice (1-7): 2

--- Tasks ---
1. [ ] Buy groceries
2. [ ] Walk the dog
3. [X] Finish report
```

**Legend:**
- `[ ]` - Incomplete task
- `[X]` - Complete task

### Updating a Task

1. Select `3` from the menu
2. Enter the task ID to update
3. Enter the new description

```
Enter choice (1-7): 3
Enter task ID to update: 1
Enter new description: Buy groceries and cook dinner
Task updated.
```

### Deleting a Task

1. Select `4` from the menu
2. Enter the task ID to delete

```
Enter choice (1-7): 4
Enter task ID to delete: 1
Task deleted.
```

### Marking Tasks Complete

1. Select `5` from the menu
2. Enter the task ID

```
Enter choice (1-7): 5
Enter task ID to mark complete: 2
Task marked as complete.
```

### Marking Tasks Incomplete

1. Select `6` from the menu
2. Enter the task ID

```
Enter choice (1-7): 6
Enter task ID to mark incomplete: 2
Task marked as incomplete.
```

### Exiting the Application

Select `7` to exit:

```
Enter choice (1-7): 7
Goodbye!
```

## Error Handling

The application handles invalid inputs gracefully:

### Invalid Menu Choice

```
Enter choice (1-7): 9
Invalid choice. Please enter 1-7.
```

### Invalid Task ID

```
Enter choice (1-7): 3
Enter task ID to update: 999
Error: Task 999 not found.
```

### Non-numeric Task ID

```
Enter choice (1-7): 3
Enter task ID to update: abc
Error: Please enter a valid number.
```

### Empty Description

```
Enter choice (1-7): 1
Enter task description:
Error: Task description cannot be empty.
```

## Complete Usage Example

```
=== Todo Application ===

--- Menu ---
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Mark Complete
6. Mark Incomplete
7. Exit
Enter choice (1-7): 1
Enter task description: Learn Python
Task added (ID: 1)

--- Menu ---
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Mark Complete
6. Mark Incomplete
7. Exit
Enter choice (1-7): 1
Enter task description: Build a todo app
Task added (ID: 2)

--- Menu ---
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Mark Complete
6. Mark Incomplete
7. Exit
Enter choice (1-7): 1
Enter task description: Read documentation
Task added (ID: 3)

--- Menu ---
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Mark Complete
6. Mark Incomplete
7. Exit
Enter choice (1-7): 2

--- Tasks ---
1. [ ] Learn Python
2. [ ] Build a todo app
3. [ ] Read documentation

--- Menu ---
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Mark Complete
6. Mark Incomplete
7. Exit
Enter choice (1-7): 5
Enter task ID to mark complete: 1
Task marked as complete.

--- Menu ---
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Mark Complete
6. Mark Incomplete
7. Exit
Enter choice (1-7): 2

--- Tasks ---
1. [X] Learn Python
2. [ ] Build a todo app
3. [ ] Read documentation

--- Menu ---
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Mark Complete
6. Mark Incomplete
7. Exit
Enter choice (1-7): 7
Goodbye!
```

## Developer Guide

### Project Structure

```
.
├── todo.py              # Main application
├── tests/               # Test suite
│   ├── __init__.py
│   ├── conftest.py      # Pytest fixtures
│   ├── test_models.py   # Task dataclass tests
│   ├── test_service.py  # Business logic tests
│   └── test_cli.py      # CLI integration tests
├── specs/               # Design documents
│   └── 1-console-todo/
│       ├── spec.md      # Feature specification
│       ├── plan.md      # Technical plan
│       ├── data-model.md
│       ├── tasks.md     # Implementation tasks
│       └── quickstart.md
├── README.md            # This file
└── .gitignore
```

### Architecture

The application follows clean architecture principles:

```
┌─────────────────────────────────────────┐
│              todo.py                     │
│  ┌─────────────┐  ┌───────────────────┐  │
│  │    CLI      │  │   TaskService     │  │
│  │ (Interface) │  │  (Business Logic) │  │
│  └─────────────┘  └───────────────────┘  │
│         │                  │              │
│         └────────┬─────────┘              │
│                  ▼                        │
│           ┌───────────┐                   │
│           │   Task    │                   │
│           │ (Data)    │                   │
│           └───────────┘                   │
│                  │                        │
│                  ▼                        │
│         ┌─────────────┐                   │
│         │ task_store  │                   │
│         │  (dict)     │                   │
│         └─────────────┘                   │
└─────────────────────────────────────────┘
```

### Running Tests

```bash
# Run all tests
python -m pytest tests/ -v

# Run with coverage
python -m pytest tests/ --cov=todo --cov-report=term-missing
```

### Test Structure

| File | Tests | Purpose |
|------|-------|---------|
| `test_models.py` | 8 | Task dataclass behavior |
| `test_service.py` | 20 | Business logic |
| `test_cli.py` | 19 | User interface |

### Key Classes

#### Task (dataclass)

```python
@dataclass
class Task:
    id: int          # Unique identifier (1, 2, 3, ...)
    description: str # Task description
    status: bool     # False = incomplete, True = complete
```

#### TaskService

Manages task operations without CLI knowledge:

- `add_task(description)` - Create new task
- `get_all_tasks()` - Return sorted list
- `update_task(id, description)` - Modify task
- `delete_task(id)` - Remove task
- `mark_complete(id)` - Mark as done
- `mark_incomplete(id)` - Mark as not done

#### CLI

Handles user interaction:

- `run()` - Main application loop
- `_display_menu()` - Show options
- `_handle_add/update/view/delete/toggle()` - Feature handlers
- `_get_valid_task_id()` - Input validation

## Limitations (Phase I)

This is Phase I of the Evolution of Todo project. Current limitations:

- **No persistence** - Tasks are lost when the application closes
- **Single user** - No user accounts or authentication
- **No search** - Cannot search or filter tasks
- **No categories** - No tags, priorities, or due dates
- **Console only** - No web or API interface

## Future Phases

Future phases will add:

- **Phase II**: Web API with FastAPI, Neon DB persistence
- **Phase III**: Next.js frontend, AI agent integration
- **Phase IV**: Multi-agent system, Docker/Kubernetes
- **Phase V**: Production deployment, Kafka/Dapr

## Contributing

This project follows Spec-Driven Development (SDD):

1. **Constitution** → `.specify/memory/constitution.md`
2. **Specification** → `specs/<feature>/spec.md`
3. **Plan** → `specs/<feature>/plan.md`
4. **Tasks** → `specs/<feature>/tasks.md`
5. **Implementation** → `/sp.implement`

## License

This project is part of the Evolution of Todo hackathon series.

## Version

- Phase: I
- Version: 1.0.0
- Date: 2026-01-02
