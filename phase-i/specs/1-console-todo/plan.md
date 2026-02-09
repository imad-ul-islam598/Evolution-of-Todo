# Implementation Plan: Console Todo Application

**Branch**: `1-console-todo` | **Date**: 2026-01-02 | **Spec**: [spec.md](./spec.md)

## Summary

Single-file Python console application for managing in-memory todo tasks. Implements CRUD operations (Add, View, Update, Delete, Toggle Complete) through a menu-driven interface. Data persists in memory for session duration only. No persistence, no external dependencies beyond Python standard library.

## Technical Context

**Language/Version**: Python 3.11+ (standard library only)
**Primary Dependencies**: None (stdlib only)
**Storage**: In-memory dictionary (session-scoped)
**Testing**: pytest (stdlib unittest as fallback)
**Target Platform**: Terminal/Console (cross-platform)
**Project Type**: Single CLI application
**Performance Goals**: Sub-second response for all operations (< 1s)
**Constraints**: No databases, no files, no external services, no web frameworks
**Scale/Scope**: Single user, up to 50 tasks (SC-005)

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Check | Status | Evidence |
|-------|--------|----------|
| Spec-Driven Development | PASS | Plan derived from approved spec.md |
| No code without approved artifacts | PASS | No implementation in this plan |
| Phase scope enforcement | PASS | Only Phase I features included |
| No future-phase concepts | PASS | No web/API/DB infrastructure |
| Technology constraints | PASS | Python stdlib only, matches mandate |
| Clean architecture | PASS | Separation of concerns defined |
| Testable design | PASS | Pure functions, injectable components |

## Project Structure

### Documentation (this feature)

```text
specs/1-console-todo/
├── plan.md              # This file
├── research.md          # N/A - no external research needed
├── data-model.md        # Phase 1 output
├── quickstart.md        # Phase 1 output
├── contracts/           # N/A - no external contracts
└── tasks.md             # Phase 2 output (/sp.tasks command)
```

### Source Code (repository root)

```text
todo.py                 # Single-file application (all-in-one)

tests/
├── conftest.py         # pytest fixtures
├── test_models.py      # Task model tests
├── test_service.py     # TaskService tests
└── test_cli.py         # CLI interface tests
```

**Structure Decision**: Single-file application for simplicity (Phase I scope). Future phases may refactor into modular structure.

## Application Architecture

### Component Diagram

```
┌─────────────────────────────────────────┐
│           todo.py (ENTRY POINT)         │
│  ┌───────────────────────────────────┐  │
│  │         main() function           │  │
│  │    Menu loop & user input         │  │
│  └───────────────────────────────────┘  │
│                  │                     │
│                  ▼                     │
│  ┌───────────────────────────────────┐  │
│  │         CLI Interface             │  │
│  │  (display_menu, get_input, etc.)  │  │
│  └───────────────────────────────────┘  │
│                  │                     │
│                  ▼                     │
│  ┌───────────────────────────────────┐  │
│  │        TaskService                │  │
│  │  (add_task, get_tasks, etc.)      │  │
│  └───────────────────────────────────┘  │
│                  │                     │
│                  ▼                     │
│  ┌───────────────────────────────────┐  │
│  │          Task (dataclass)         │  │
│  │    id, description, status        │  │
│  └───────────────────────────────────┘  │
│                  │                     │
│                  ▼                     │
│  ┌───────────────────────────────────┐  │
│  │     task_store (dict)             │  │
│  │  {id: Task, id: Task, ...}        │  │
│  └───────────────────────────────────┘  │
└─────────────────────────────────────────┘
```

### File Structure

```
todo.py
├── Task (dataclass)
│   ├── id: int
│   ├── description: str
│   └── status: bool
│
├── TaskService (class)
│   ├── __init__(self, task_store: dict)
│   ├── add_task(description: str) -> Task
│   ├── get_all_tasks() -> list[Task]
│   ├── update_task(task_id: int, new_description: str) -> Task | None
│   ├── delete_task(task_id: int) -> bool
│   ├── mark_complete(task_id: int) -> Task | None
│   ├── mark_incomplete(task_id: int) -> Task | None
│   └── _generate_id() -> int
│
├── CLI (class)
│   ├── __init__(self, task_service: TaskService)
│   ├── run() -> None
│   ├── _display_menu() -> str
│   ├── _handle_add() -> None
│   ├── _handle_view() -> None
│   ├── _handle_update() -> None
│   ├── _handle_delete() -> None
│   ├── _handle_toggle() -> None
│   └── _get_valid_task_id() -> int | None
│
└── main() -> None
```

## Data Design

### Task Entity

```python
@dataclass
class Task:
    """Represents a single todo item."""
    id: int                      # Unique positive integer (1, 2, 3, ...)
    description: str             # Non-empty task description
    status: bool                 # False = incomplete, True = complete
```

### In-Memory Storage

```python
# Global task store (session-scoped)
task_store: dict[int, Task] = {}
```

**Why dictionary over list**:
- O(1) lookup by ID for update/delete operations (vs O(n) list search)
- Direct mapping from ID to Task simplifies error handling
- Automatic uniqueness enforcement on IDs

**ID Generation Strategy**:
```python
next_task_id: int = 1  # Global counter, never decrements
```

Sequential IDs starting from 1. IDs never reused after deletion (per spec assumption).

## Control Flow

### Main Loop

```
┌──────────────────────┐
│   Start Application  │
└──────────┬───────────┘
           ▼
┌──────────────────────┐
│  Display Menu        │
│  1. Add Task         │
│  2. View Tasks       │
│  3. Update Task      │
│  4. Delete Task      │
│  5. Mark Complete    │
│  6. Mark Incomplete  │
│  7. Exit             │
└──────────┬───────────┘
           ▼
    ┌──────────────────┐
    │ Get User Input   │
    └──────────┬───────┘
               ▼
    ┌──────────────────┐
    │ Validate Input   │
    └──────────┬───────┘
               ▼
    ┌──────────────────┐
    │ Dispatch to      │
    │ Handler          │
    └──────────┬───────┘
               ▼
    ┌──────────────────┐
    │ Display Result/  │
    │ Error            │
    └──────────┬───────┘
               ▼
    ┌──────────────────┐
    │ Exit Requested?  │
    │  (Option 7)      │
    ├────────┬─────────┤
    │   No   │   Yes   │
    │   ├────▼┐        │
    │   │Loop│        │
    │   └─────┘        │
    └──────────────────┘
```

### User Input Handling

```python
def get_menu_choice() -> str:
    """Get and validate menu choice from user."""
    while True:
        choice = input("Enter choice (1-7): ").strip()
        if choice in {"1", "2", "3", "4", "5", "6", "7"}:
            return choice
        print("Invalid choice. Please enter 1-7.")
```

### Input Validation Strategy

| Input Type | Validation | Error Message |
|------------|------------|---------------|
| Menu choice | Must be 1-7 digit | "Invalid choice. Please enter 1-7." |
| Task ID | Must be positive integer, exists in store | "Task with ID {id} not found." |
| Task description | Must be non-empty after strip | "Task description cannot be empty." |

## Separation of Concerns

### TaskService (Business Logic)

Handles all task operations without knowledge of CLI details:

```python
class TaskService:
    """Business logic for task management."""

    def __init__(self, task_store: dict[int, Task] | None = None):
        self._task_store = task_store if task_store is not None else {}
        self._next_id = 1

    def add_task(self, description: str) -> Task:
        """Create a new task."""
        if not description or not description.strip():
            raise ValueError("Description cannot be empty")

        task = Task(id=self._generate_id(), description=description.strip(), status=False)
        self._task_store[task.id] = task
        return task

    def get_all_tasks(self) -> list[Task]:
        """Return all tasks sorted by ID."""
        return sorted(self._task_store.values(), key=lambda t: t.id)

    def update_task(self, task_id: int, new_description: str) -> Task | None:
        """Update task description. Returns None if not found."""
        if task_id not in self._task_store:
            return None
        if not new_description or not new_description.strip():
            raise ValueError("Description cannot be empty")

        task = self._task_store[task_id]
        task.description = new_description.strip()
        return task

    def delete_task(self, task_id: int) -> bool:
        """Delete task by ID. Returns True if deleted, False if not found."""
        return self._task_store.pop(task_id, None) is not None

    def mark_complete(self, task_id: int) -> Task | None:
        """Mark task as complete."""
        return self._update_status(task_id, True)

    def mark_incomplete(self, task_id: int) -> Task | None:
        """Mark task as incomplete."""
        return self._update_status(task_id, False)

    def _update_status(self, task_id: int, status: bool) -> Task | None:
        """Internal status update helper."""
        task = self._task_store.get(task_id)
        if task is None:
            return None
        task.status = status
        return task

    def _generate_id(self) -> int:
        """Generate next sequential ID."""
        current_id = self._next_id
        self._next_id += 1
        return current_id
```

### CLI (User Interface)

Handles all user interaction, input/output formatting:

```python
class CLI:
    """Console interface for task management."""

    def __init__(self, task_service: TaskService):
        self._service = task_service

    def run(self) -> None:
        """Main application loop."""
        print("=== Todo Application ===")
        while True:
            self._display_menu()
            choice = self._get_menu_choice()

            if choice == "7":
                print("Goodbye!")
                break

            self._handle_choice(choice)

    def _display_menu(self) -> None:
        """Display the main menu."""
        print("\n--- Menu ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Complete")
        print("6. Mark Incomplete")
        print("7. Exit")

    def _get_menu_choice(self) -> str:
        """Get validated menu choice."""
        while True:
            choice = input("Enter choice (1-7): ").strip()
            if choice in {"1", "2", "3", "4", "5", "6", "7"}:
                return choice
            print("Invalid choice. Please enter 1-7.")

    def _handle_choice(self, choice: str) -> None:
        """Route to appropriate handler."""
        handlers = {
            "1": self._handle_add,
            "2": self._handle_view,
            "3": self._handle_update,
            "4": self._handle_delete,
            "5": lambda: self._handle_toggle(complete=True),
            "6": lambda: self._handle_toggle(complete=False),
        }
        handler = handlers.get(choice)
        if handler:
            handler()

    def _handle_add(self) -> None:
        """Handle add task flow."""
        description = input("Enter task description: ").strip()
        if not description:
            print("Error: Task description cannot be empty.")
            return

        task = self._service.add_task(description)
        print(f"Task added (ID: {task.id})")

    def _handle_view(self) -> None:
        """Handle view tasks flow."""
        tasks = self._service.get_all_tasks()
        if not tasks:
            print("No tasks yet. Add one!")
            return

        print("\n--- Tasks ---")
        for task in tasks:
            status = "[X]" if task.status else "[ ]"
            print(f"{task.id}. {status} {task.description}")

    def _handle_update(self) -> None:
        """Handle update task flow."""
        task_id = self._get_valid_task_id("Enter task ID to update: ")
        if task_id is None:
            return

        new_desc = input("Enter new description: ").strip()
        if not new_desc:
            print("Error: Description cannot be empty.")
            return

        result = self._service.update_task(task_id, new_desc)
        if result:
            print("Task updated.")
        else:
            print(f"Error: Task {task_id} not found.")

    def _handle_delete(self) -> None:
        """Handle delete task flow."""
        task_id = self._get_valid_task_id("Enter task ID to delete: ")
        if task_id is None:
            return

        if self._service.delete_task(task_id):
            print("Task deleted.")
        else:
            print(f"Error: Task {task_id} not found.")

    def _handle_toggle(self, complete: bool) -> None:
        """Handle mark complete/incomplete flow."""
        action = "complete" if complete else "incomplete"
        task_id = self._get_valid_task_id(f"Enter task ID to mark {action}: ")
        if task_id is None:
            return

        if complete:
            result = self._service.mark_complete(task_id)
        else:
            result = self._service.mark_incomplete(task_id)

        if result:
            print(f"Task marked as {action}.")
        else:
            print(f"Error: Task {task_id} not found.")

    def _get_valid_task_id(self, prompt: str) -> int | None:
        """Get a valid task ID from user input."""
        while True:
            try:
                user_input = input(prompt).strip()
                if not user_input:
                    return None
                task_id = int(user_input)
                if task_id <= 0:
                    print("Error: Task ID must be a positive number.")
                    continue
                return task_id
            except ValueError:
                print("Error: Please enter a valid number.")
```

## Error Handling Strategy

### Error Classes

```python
class TaskNotFoundError(ValueError):
    """Raised when a task ID does not exist."""
    pass


class EmptyDescriptionError(ValueError):
    """Raised when task description is empty."""
    pass
```

### Error Handling Map

| Operation | Error Condition | Handler Response |
|-----------|-----------------|------------------|
| Add | Empty description | Print "Error: Task description cannot be empty." |
| Update | Invalid ID | Print "Error: Task {id} not found." |
| Update | Empty description | Print "Error: Description cannot be empty." |
| Delete | Invalid ID | Print "Error: Task {id} not found." |
| Mark Complete | Invalid ID | Print "Error: Task {id} not found." |
| Mark Incomplete | Invalid ID | Print "Error: Task {id} not found." |
| Any | Non-numeric ID input | Print "Error: Please enter a valid number." |

### Graceful Degradation

- Invalid input does not crash application
- User can retry after error messages
- Session continues until explicit exit

## Entry Point

```python
def main() -> None:
    """Application entry point."""
    task_store: dict[int, Task] = {}
    service = TaskService(task_store)
    cli = CLI(service)
    cli.run()


if __name__ == "__main__":
    main()
```

## Testing Strategy

### Test Categories

| Category | Location | Purpose |
|----------|----------|---------|
| Unit - Models | tests/test_models.py | Task dataclass behavior |
| Unit - Service | tests/test_service.py | Business logic without CLI |
| Integration - CLI | tests/test_cli.py | Full user flows |

### Key Test Scenarios

```python
# test_models.py
def test_task_creation():
    task = Task(id=1, description="Test task", status=False)
    assert task.id == 1
    assert task.description == "Test task"
    assert task.status is False


# test_service.py
def test_add_task():
    store = {}
    service = TaskService(store)
    task = service.add_task("New task")
    assert task.id == 1
    assert task.description == "New task"
    assert task.status is False
    assert store[1] == task


def test_get_nonexistent_task():
    store = {}
    service = TaskService(store)
    result = service.update_task(999, "New description")
    assert result is None


# test_cli.py
def test_view_empty_list(capsys):
    store = {}
    service = TaskService(store)
    cli = CLI(service)
    cli._handle_view()
    captured = capsys.readouterr()
    assert "No tasks yet" in captured.out
```

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| (None) | This plan follows all constitution requirements | N/A |

## Out of Scope

Per Phase I specification, the following are explicitly excluded:

- Any form of persistence (files, database)
- Multiple users or sessions
- Categories, tags, priorities, or due dates
- Search or filtering functionality
- Undo/redo operations
- Import/export capabilities
- Web interface or API
- Configuration files
- Logging (beyond console output)

## Next Steps

After plan approval:
1. Run `/sp.tasks` to generate testable implementation tasks
2. Implement following Red-Green-Refactor cycle
3. Ensure 80%+ test coverage on business logic
