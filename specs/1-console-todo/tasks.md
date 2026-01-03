# Tasks: Console Todo Application

**Input**: Design documents from `/specs/1-console-todo/`
**Prerequisites**: plan.md, spec.md, data-model.md

**Organization**: Tasks are grouped to enable independent implementation and testing of each user story

**Status**: ALL TASKS COMPLETED - Phase I Implementation Ready

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2)
- Include exact file paths in descriptions

---

## Phase 1: Foundation (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**CRITICAL**: No user story work can begin until this phase is complete

### Infrastructure Setup

- [x] T001 [P] Create tests directory structure at repository root
  - **Preconditions**: None
  - **Expected Output**: `tests/` directory with `__init__.py`
  - **Artifacts**: `tests/__init__.py`

- [x] T002 [P] Create pytest configuration in tests/conftest.py
  - **Preconditions**: T001 complete
  - **Expected Output**: Pytest fixtures available for all tests
  - **Artifacts**: `tests/conftest.py`
  - **Reference**: plan.md "Testing Strategy"

- [x] T003 Create Task dataclass in todo.py (lines 104-108)
  - **Preconditions**: None
  - **Expected Output**: Task class with id, description, status fields
  - **Artifacts**: `todo.py` - Task dataclass
  - **Reference**: data-model.md "Task Entity", plan.md "File Structure"

- [x] T004 Create TaskService class with __init__ and _generate_id in todo.py (lines 110-119)
  - **Preconditions**: T003 complete
  - **Expected Output**: TaskService class with task_store and ID counter
  - **Artifacts**: `todo.py` - TaskService class (constructor and ID generation)
  - **Reference**: plan.md "TaskService (Business Logic)", data-model.md "ID Generation"

- [x] T005 Create CLI class with __init__ in todo.py (lines 120-122)
  - **Preconditions**: T004 complete
  - **Expected Output**: CLI class with task_service dependency
  - **Artifacts**: `todo.py` - CLI class constructor
  - **Reference**: plan.md "CLI (class)", "Separation of Concerns"

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 2: Add Task (User Story 1 - P1) MVP

**Goal**: Users can add new tasks to their todo list

**Independent Test**: Launch app, select "Add Task", enter description, verify task appears in list

**Reference**: spec.md "User Story 1 - Add New Tasks", plan.md "TaskService.add_task"

### Tests for Add Task

- [x] T006 [P] [US1] Unit test for Task dataclass in tests/test_models.py
  - **Preconditions**: T003 complete
  - **Expected Output**: Tests for Task creation and field access
  - **Artifacts**: `tests/test_models.py`
  - **Reference**: plan.md "test_models.py"

- [x] T007 [P] [US1] Unit test for TaskService.add_task in tests/test_service.py
  - **Preconditions**: T004, T006 complete
  - **Expected Output**: Tests that verify task creation and storage
  - **Artifacts**: `tests/test_service.py`
  - **Reference**: plan.md "test_service.py", "Key Test Scenarios"

### Implementation for Add Task

- [x] T008 [US1] Implement TaskService.add_task() in todo.py (lines 249-256)
  - **Preconditions**: T004 complete
  - **Expected Output**: add_task(description) creates and stores Task
  - **Artifacts**: `todo.py` - TaskService.add_task method
  - **Reference**: plan.md lines 249-256

- [x] T009 [US1] Implement CLI._display_menu() in todo.py (lines 324-333)
  - **Preconditions**: T005 complete
  - **Expected Output**: Menu displayed with options 1-7
  - **Artifacts**: `todo.py` - CLI._display_menu method
  - **Reference**: plan.md "Main Loop", "User Input Handling"

- [x] T010 [US1] Implement CLI._handle_add() in todo.py (lines 357-365)
  - **Preconditions**: T005, T008 complete
  - **Expected Output**: User can input description, task added, confirmation shown
  - **Artifacts**: `todo.py` - CLI._handle_add method
  - **Reference**: plan.md lines 357-365

**Checkpoint**: Add Task feature complete and testable

---

## Phase 3: View Tasks (User Story 2 - P1) MVP

**Goal**: Users can see all their tasks with completion status

**Independent Test**: Add tasks, select "View Tasks", verify all tasks displayed

**Reference**: spec.md "User Story 2 - View Task List", plan.md "TaskService.get_all_tasks"

### Tests for View Tasks

- [x] T011 [P] [US2] Unit test for TaskService.get_all_tasks in tests/test_service.py
  - **Preconditions**: T004 complete
  - **Expected Output**: Tests for retrieving all tasks sorted by ID
  - **Artifacts**: `tests/test_service.py` additions
  - **Reference**: plan.md "Key Test Scenarios"

- [x] T012 [P] [US2] Integration test for CLI._handle_view in tests/test_cli.py
  - **Preconditions**: T005, T014 complete
  - **Expected Output**: Tests for view functionality with empty and non-empty lists
  - **Artifacts**: `tests/test_cli.py`
  - **Reference**: plan.md "test_cli.py"

### Implementation for View Tasks

- [x] T013 [US2] Implement TaskService.get_all_tasks() in todo.py (lines 258-260)
  - **Preconditions**: T004 complete
  - **Expected Output**: get_all_tasks() returns sorted list of all tasks
  - **Artifacts**: `todo.py` - TaskService.get_all_tasks method
  - **Reference**: plan.md lines 258-260

- [x] T014 [US2] Implement CLI._handle_view() in todo.py (lines 367-377)
  - **Preconditions**: T005, T013 complete
  - **Expected Output**: Tasks displayed with [X]/[ ] status indicators
  - **Artifacts**: `todo.py` - CLI._handle_view method
  - **Reference**: plan.md lines 367-377

**Checkpoint**: View Tasks feature complete and testable

---

## Phase 4: Update Task (User Story 3 - P2)

**Goal**: Users can modify existing task descriptions

**Independent Test**: Add task, select "Update Task", change description, verify update

**Reference**: spec.md "User Story 3 - Update Task", plan.md "TaskService.update_task"

### Tests for Update Task

- [x] T015 [P] [US3] Unit test for TaskService.update_task in tests/test_service.py
  - **Preconditions**: T004 complete
  - **Expected Output**: Tests for updating description, invalid ID handling
  - **Artifacts**: `tests/test_service.py` additions
  - **Reference**: plan.md "Key Test Scenarios"

- [x] T016 [P] [US3] Integration test for CLI._handle_update in tests/test_cli.py
  - **Preconditions**: T005, T018 complete
  - **Expected Output**: Tests for update flow with valid/invalid inputs
  - **Artifacts**: `tests/test_cli.py` additions

### Implementation for Update Task

- [x] T017 [US3] Implement TaskService.update_task() in todo.py (lines 262-271)
  - **Preconditions**: T004 complete
  - **Expected Output**: update_task(id, description) updates or returns None
  - **Artifacts**: `todo.py` - TaskService.update_task method
  - **Reference**: plan.md lines 262-271

- [x] T018 [US3] Implement CLI._handle_update() in todo.py (lines 379-394)
  - **Preconditions**: T005, T017 complete
  - **Expected Output**: User can update task description with validation
  - **Artifacts**: `todo.py` - CLI._handle_update method
  - **Reference**: plan.md lines 379-394

**Checkpoint**: Update Task feature complete and testable

---

## Phase 5: Delete Task (User Story 4 - P2)

**Goal**: Users can remove tasks from their list

**Independent Test**: Add tasks, select "Delete Task", verify task removed

**Reference**: spec.md "User Story 4 - Delete Task", plan.md "TaskService.delete_task"

### Tests for Delete Task

- [x] T019 [P] [US4] Unit test for TaskService.delete_task in tests/test_service.py
  - **Preconditions**: T004 complete
  - **Expected Output**: Tests for deleting task, invalid ID handling
  - **Artifacts**: `tests/test_service.py` additions

- [x] T020 [P] [US4] Integration test for CLI._handle_delete in tests/test_cli.py
  - **Preconditions**: T005, T022 complete
  - **Expected Output**: Tests for delete flow with valid/invalid IDs
  - **Artifacts**: `tests/test_cli.py` additions

### Implementation for Delete Task

- [x] T021 [US4] Implement TaskService.delete_task() in todo.py (lines 273-275)
  - **Preconditions**: T004 complete
  - **Expected Output**: delete_task(id) returns True if deleted, False if not found
  - **Artifacts**: `todo.py` - TaskService.delete_task method
  - **Reference**: plan.md lines 273-275

- [x] T022 [US4] Implement CLI._handle_delete() in todo.py (lines 396-405)
  - **Preconditions**: T005, T021 complete
  - **Expected Output**: User can delete task by ID
  - **Artifacts**: `todo.py` - CLI._handle_delete method
  - **Reference**: plan.md lines 396-405

**Checkpoint**: Delete Task feature complete and testable

---

## Phase 6: Mark Complete/Incomplete (User Story 5 - P2)

**Goal**: Users can toggle task completion status

**Independent Test**: Add task, mark complete, verify [X], mark incomplete, verify [ ]

**Reference**: spec.md "User Story 5 - Mark Task Complete/Incomplete", plan.md "TaskService.mark_complete/mark_incomplete"

### Tests for Mark Complete/Incomplete

- [x] T023 [P] [US5] Unit test for mark_complete/mark_incomplete in tests/test_service.py
  - **Preconditions**: T004 complete
  - **Expected Output**: Tests for status toggling, invalid ID handling
  - **Artifacts**: `tests/test_service.py` additions

- [x] T024 [P] [US5] Integration test for CLI._handle_toggle in tests/test_cli.py
  - **Preconditions**: T005, T026 complete
  - **Expected Output**: Tests for toggle flow with complete/incomplete
  - **Artifacts**: `tests/test_cli.py` additions

### Implementation for Mark Complete/Incomplete

- [x] T025 [US5] Implement TaskService._update_status() helper in todo.py (lines 285-291)
  - **Preconditions**: T004 complete
  - **Expected Output**: Internal helper for status updates
  - **Artifacts**: `todo.py` - TaskService._update_status method
  - **Reference**: plan.md lines 285-291

- [x] T026 [US5] Implement TaskService.mark_complete() in todo.py (lines 277-279)
  - **Preconditions**: T025 complete
  - **Expected Output**: mark_complete(id) sets status to True
  - **Artifacts**: `todo.py` - TaskService.mark_complete method
  - **Reference**: plan.md lines 277-279

- [x] T027 [US5] Implement TaskService.mark_incomplete() in todo.py (lines 281-283)
  - **Preconditions**: T025 complete
  - **Expected Output**: mark_incomplete(id) sets status to False
  - **Artifacts**: `todo.py` - TaskService.mark_incomplete method
  - **Reference**: plan.md lines 281-283

- [x] T028 [US5] Implement CLI._handle_toggle() in todo.py (lines 407-422)
  - **Preconditions**: T005, T026, T027 complete
  - **Expected Output**: User can toggle task status via menu
  - **Artifacts**: `todo.py` - CLI._handle_toggle method
  - **Reference**: plan.md lines 407-422

**Checkpoint**: Mark Complete/Incomplete feature complete and testable

---

## Phase 7: Input Validation and Error Handling

**Goal**: Robust handling of invalid inputs with user-friendly messages

**Reference**: plan.md "Error Handling Strategy", "Input Validation Strategy"

### Tests for Error Handling

- [x] T029 [P] Unit tests for input validation errors in tests/test_service.py
  - **Preconditions**: T004 complete
  - **Expected Output**: Tests for empty description handling
  - **Artifacts**: `tests/test_service.py` additions

- [x] T030 [P] Integration tests for error messages in tests/test_cli.py
  - **Preconditions**: T005 complete
  - **Expected Output**: Tests verifying error messages are displayed
  - **Artifacts**: `tests/test_cli.py` additions
  - **Reference**: plan.md "Error Handling Map"

### Implementation for Input Validation

- [x] T031 [P] Implement CLI._get_valid_task_id() in todo.py (lines 424-437)
  - **Preconditions**: T005 complete
  - **Expected Output**: Validates numeric input, positive ID, returns None on empty
  - **Artifacts**: `todo.py` - CLI._get_valid_task_id method
  - **Reference**: plan.md lines 424-437

- [x] T032 [P] Add description validation in CLI._handle_add (todo.py lines 360-362)
  - **Preconditions**: T010 complete
  - **Expected Output**: Empty description shows error, no task created
  - **Artifacts**: `todo.py` modifications to _handle_add
  - **Reference**: plan.md "Input Validation Strategy"

- [x] T033 [P] Add description validation in CLI._handle_update (todo.py lines 385-388)
  - **Preconditions**: T018 complete
  - **Expected Output**: Empty description shows error, no update applied
  - **Artifacts**: `todo.py` modifications to _handle_update
  - **Reference**: plan.md "Input Validation Strategy"

**Checkpoint**: Input validation complete for all operations

---

## Phase 8: Application Startup and Exit Flow

**Goal**: Complete menu loop and application lifecycle

**Reference**: plan.md "Main Loop", "Entry Point"

### Tests for Application Flow

- [x] T034 Integration test for menu loop and exit in tests/test_cli.py
  - **Preconditions**: T005, T035 complete
  - **Expected Output**: Test can run full menu cycle and exit cleanly
  - **Artifacts**: `tests/test_cli.py` additions

### Implementation for Application Flow

- [x] T035 [P] Implement CLI._get_menu_choice() in todo.py (lines 335-341)
  - **Preconditions**: T005 complete
  - **Expected Output**: Validates menu input 1-7, loops on invalid
  - **Artifacts**: `todo.py` - CLI._get_menu_choice method
  - **Reference**: plan.md lines 335-341

- [x] T036 [P] Implement CLI._handle_choice() dispatcher in todo.py (lines 343-355)
  - **Preconditions**: T005 complete
  - **Expected Output**: Routes menu choice to appropriate handler
  - **Artifacts**: `todo.py` - CLI._handle_choice method
  - **Reference**: plan.md lines 343-355

- [x] T037 Implement CLI.run() main loop in todo.py (lines 311-322)
  - **Preconditions**: T009, T014, T018, T022, T028, T035, T036 complete
  - **Expected Output**: Main loop displays menu, handles choices, exits on option 7
  - **Artifacts**: `todo.py` - CLI.run method
  - **Reference**: plan.md lines 311-322

- [x] T038 Implement main() entry point in todo.py (lines 476-486)
  - **Preconditions**: T037 complete
  - **Expected Output**: Application starts via `python todo.py`
  - **Artifacts**: `todo.py` - main() function and `if __name__ == "__main__"`
  - **Reference**: plan.md "Entry Point"

**Checkpoint**: Full application complete and runnable

---

## Phase 9: Integration and Validation

**Goal**: Verify all features work together, ensure test coverage

- [x] T039 Run full test suite and verify 80%+ coverage on TaskService
  - **Preconditions**: All previous tasks complete
  - **Expected Output**: All tests pass, coverage target met
  - **Artifacts**: Test execution results

- [x] T040 Manual validation of all user stories
  - **Preconditions**: T039 complete
  - **Expected Output**: All 5 CRUD operations work without errors
  - **Artifacts**: Validation checklist

- [x] T041 Verify quickstart.md examples work
  - **Preconditions**: All implementation complete
  - **Expected Output**: Running application matches quickstart.md
  - **Artifacts**: Confirmed working examples

---

## Summary

| Metric | Value |
|--------|-------|
| Total Tasks | 41 |
| Completed | 41 |
| Test Files | 3 |
| Source Files | 1 |

## Source Files Created

| File | Description |
|------|-------------|
| `todo.py` | Main application (Task, TaskService, CLI classes) |
| `tests/__init__.py` | Tests package marker |
| `tests/conftest.py` | Pytest fixtures |
| `tests/test_models.py` | Task dataclass tests (8 tests) |
| `tests/test_service.py` | TaskService tests (20 tests) |
| `tests/test_cli.py` | CLI integration tests (19 tests) |

## Application Features

1. **Add Task** - Create new tasks with descriptions
2. **View Tasks** - Display all tasks with completion status
3. **Update Task** - Modify task descriptions by ID
4. **Delete Task** - Remove tasks by ID
5. **Mark Complete** - Toggle task to complete status
6. **Mark Incomplete** - Toggle task to incomplete status

## Running the Application

```bash
python todo.py
```

## Running Tests

```bash
python -m pytest tests/ -v
```
