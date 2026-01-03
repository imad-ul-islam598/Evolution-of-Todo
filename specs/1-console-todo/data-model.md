# Data Model: Console Todo Application

## Entity: Task

Represents a single todo item stored in memory for the session duration.

### Attributes

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| `id` | `int` | Positive, unique, sequential | Unique identifier (1, 2, 3, ...) |
| `description` | `str` | Non-empty, stripped | Task text (whitespace trimmed) |
| `status` | `bool` | Required | `False` = incomplete, `True` = complete |

### Validation Rules

1. **ID Validation**
   - Must be a positive integer (1+)
   - Must exist in task_store to be operated on
   - Never reused after deletion

2. **Description Validation**
   - Must not be empty after `strip()`
   - Leading/trailing whitespace removed on storage
   - Internal whitespace preserved

3. **Status Validation**
   - Boolean value only
   - Toggled via `mark_complete()` / `mark_incomplete()`

### State Transitions

```
[incomplete] ──mark_complete()──► [complete]
     ▲                              │
     └────mark_incomplete()────────┘
```

### Python Definition

```python
from dataclasses import dataclass


@dataclass
class Task:
    """Represents a single todo item."""
    id: int
    description: str
    status: bool = False
```

## Storage: task_store

In-memory dictionary mapping task IDs to Task objects.

```python
task_store: dict[int, Task] = {}
```

### Storage Properties

| Property | Value |
|----------|-------|
| Type | Python `dict` |
| Key | `int` (task ID) |
| Value | `Task` instance |
| Scope | Session lifetime |
| Capacity | Unlimited (practical limit ~50 per SC-005) |

### Access Patterns

| Operation | Method | Complexity |
|-----------|--------|------------|
| Create | `task_store[id] = task` | O(1) |
| Read by ID | `task_store.get(id)` | O(1) |
| Update | `task_store[id].field = value` | O(1) |
| Delete | `task_store.pop(id)` | O(1) |
| List all | `list(task_store.values())` | O(n) |

## ID Generation

### Strategy: Sequential Counter

```python
_next_task_id: int = 1  # Initial value

def _generate_id(self) -> int:
    """Generate the next sequential ID."""
    current_id = self._next_id
    self._next_id += 1
    return current_id
```

### Properties

| Property | Value |
|----------|-------|
| Starting value | 1 |
| Increment | +1 per task |
| Wrap | No |
| Reuse after delete | No |

### Rationale

- Sequential IDs are user-friendly (1, 2, 3...)
- No collision handling needed
- Simple implementation for Phase I scope
- IDs remain valid references until deleted

## Data Flow

### Create Task Flow

```
User Input (description)
        │
        ▼
CLI._handle_add()
        │
        ▼
TaskService.add_task(description)
        │
        ▼
Validate description (not empty)
        │
        ▼
Generate new ID (_generate_id)
        │
        ▼
Create Task(id, description, status=False)
        │
        ▼
Store in task_store[id] = task
        │
        ▼
Return Task
```

### Toggle Status Flow

```
User Input (task_id)
        │
        ▼
CLI._handle_toggle(complete=True/False)
        │
        ▼
TaskService.mark_complete/mark_incomplete(task_id)
        │
        ▼
Lookup task = task_store.get(task_id)
        │
        ▼
If not found → return None (error)
        │
        ▼
Update task.status = new_status
        │
        ▼
Return updated Task
```

## Constraints Summary

| Constraint | Enforcement |
|------------|-------------|
| ID uniqueness | Dictionary key constraint |
| ID positive | Validation on input |
| Description non-empty | Validation before storage |
| Status boolean | Python `bool` type |
| Session-only persistence | In-memory dict only |
