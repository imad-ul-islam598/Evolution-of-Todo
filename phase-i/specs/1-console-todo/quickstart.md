# Quickstart: Console Todo Application

## Running the Application

### Prerequisites

- Python 3.11 or higher
- No external dependencies (stdlib only)

### Setup

```bash
# Clone repository
git clone <repo-url>
cd built-in-memory-console-todo-app

# No pip install needed - stdlib only
```

### Run

```bash
python todo.py
```

### First Run Example

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
Enter task description: Buy groceries
Task added (ID: 1)

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
1. [ ] Buy groceries

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
1. [X] Buy groceries

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
todo.py              # Single-file application
tests/
├── __init__.py
├── conftest.py      # Pytest fixtures
├── test_models.py   # Task dataclass tests
├── test_service.py  # TaskService tests
├── test_cli.py      # CLI interface tests
```

### Running Tests

```bash
# Run all tests
python -m pytest tests/

# Run with coverage
python -m pytest tests/ --cov=todo --cov-report=term-missing

# Run specific test file
python -m pytest tests/test_service.py -v
```

### Test Coverage Target

- Minimum 80% on business logic (TaskService)
- All error paths must be tested

### Code Style

- Follow PEP 8 (enforced via tools in later phases)
- Type annotations on all public functions
- Docstrings for modules, classes, functions

### Adding a New Task (Code Walkthrough)

```python
# 1. User selects "Add Task" from menu
# 2. CLI prompts for description
description = input("Enter task description: ").strip()

# 3. Service creates task
task = service.add_task(description)

# 4. Internally:
#    - Validates description is not empty
#    - Generates new ID (1, 2, 3, ...)
#    - Creates Task(id, description, status=False)
#    - Stores in task_store[id] = task
#    - Returns Task

print(f"Task added (ID: {task.id})")
```

### Error Handling Examples

```python
# Empty description
> Enter task description:
Error: Task description cannot be empty.

# Invalid task ID
> Enter task ID to update: 999
Error: Task 999 not found.

# Non-numeric input
> Enter task ID: abc
Error: Please enter a valid number.
```

## Architecture Overview

```
todo.py
│
├── Task (dataclass)
│   └── Data container with id, description, status
│
├── TaskService (class)
│   └── Business logic: add, get, update, delete, toggle
│
├── CLI (class)
│   └── User interface: menus, input, output
│
└── main()
    └── Application entry point
```

### Separation of Concerns

| Component | Responsibility |
|-----------|----------------|
| `Task` | Data structure only |
| `TaskService` | Business rules, data operations |
| `CLI` | User interaction, formatting |
| `main` | Assembly, lifecycle |

## Troubleshooting

### "python: command not found"

Use `python3` instead of `python`:

```bash
python3 todo.py
```

### Tests failing

Ensure Python 3.11+:

```bash
python --version
```

### Menu not responding

Check for accidental newline characters in input. The CLI strips all input.
