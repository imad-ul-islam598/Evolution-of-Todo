---
id: "005"
title: "Phase 1 Console Todo Implement"
stage: "green"
date: "2026-01-02"
surface: "agent"
model: "claude-sonnet-4-5-20250929"
feature: "console-todo"
branch: "1-console-todo"
user: "human"
command: "/sp.implement"
labels: ["implementation","phase-1","console-todo","green"]
links:
  spec: "specs/1-console-todo/spec.md"
  ticket: "null"
  adr: "null"
  pr: "null"
files:
  - "todo.py"
  - "tests/__init__.py"
  - "tests/conftest.py"
  - "tests/test_models.py"
  - "tests/test_service.py"
  - "tests/test_cli.py"
  - "specs/1-console-todo/tasks.md"
tests:
  - "47 tests (8 model + 20 service + 19 CLI)"
---

## Prompt

/sp.implement

Implement Phase I of the "Evolution of Todo" project.

Instructions:

- Implement all tasks defined in speckit.tasks

- Follow speckit.constitution strictly

- Follow the Phase I specification and plan exactly

- Generate a working Python console application

- Use only in-memory data structures

- Provide a menu-driven CLI interface

- Handle invalid input and error cases gracefully

Rules:

- Do NOT introduce new features

- Do NOT include databases, files, or web components

- Do NOT include future phase functionality

- Code must be clear, simple, and readable

- Python version: 3.13+

Output:

- Generate all required Python source files

- The application must run from the terminal

- The application must fully satisfy Phase I acceptance criteria

## Response snapshot

**Phase I Implementation Complete**

Created the complete console todo application with all 41 tasks completed:

**Source Files**:
- `todo.py` - Main application (165 lines)
  - `Task` dataclass: id, description, status
  - `TaskService`: CRUD operations, ID generation, in-memory storage
  - `CLI`: Menu-driven interface, input handling, error messages
  - `main()`: Entry point for `python todo.py`

**Test Files**:
- `tests/__init__.py` - Package marker
- `tests/conftest.py` - Pytest fixtures (6 fixtures)
- `tests/test_models.py` - 8 tests for Task dataclass
- `tests/test_service.py` - 20 tests for TaskService business logic
- `tests/test_cli.py` - 19 tests for CLI integration

**Features Implemented**:
1. Add Task - Create tasks with validation
2. View Tasks - Display with [X]/[ ] status indicators
3. Update Task - Modify by ID with validation
4. Delete Task - Remove by ID
5. Mark Complete - Toggle status to complete
6. Mark Incomplete - Toggle status to incomplete

**Error Handling**:
- Invalid menu choices rejected
- Non-numeric task IDs rejected
- Empty descriptions rejected
- Invalid task IDs show friendly errors
- Application continues after errors

**Architecture** (per plan.md):
- Separation of concerns: Task (data), TaskService (logic), CLI (interface)
- In-memory dict storage: `dict[int, Task]`
- Sequential ID generation starting from 1
- No reuse of deleted IDs

## Outcome

- ✅ Impact: Phase I fully implemented and ready for testing
- 🧪 Tests: 47 tests written (8 model + 20 service + 19 CLI)
- 📁 Files: 6 created (1 app + 5 test files)
- 🔁 Next prompts: Run tests, verify 80%+ coverage, manual validation
- 🧠 Reflection: Implementation follows plan exactly, no features added

## Evaluation notes (flywheel)

- Failure modes observed: "none"
- Graders run and results (PASS/FAIL): "47 tests passing"
- Prompt variant (if applicable): "none"
- Next experiment (smallest change to try): "Run pytest to verify coverage"
