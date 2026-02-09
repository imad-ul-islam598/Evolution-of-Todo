"""Unit tests for the TaskService business logic."""

import pytest
from todo import Task, TaskService


class TestTaskServiceAddTask:
    """Tests for TaskService.add_task()."""

    def test_add_task_creates_task(self, task_service):
        """Test that add_task creates and returns a new task."""
        task = task_service.add_task("Buy groceries")
        assert task is not None
        assert task.id == 1
        assert task.description == "Buy groceries"
        assert task.status is False

    def test_add_task_stores_in_store(self, task_service):
        """Test that add_task stores the task in task_store."""
        task = task_service.add_task("New task")
        assert 1 in task_service._task_store
        assert task_service._task_store[1] == task

    def test_add_multiple_tasks_sequential_ids(self, task_service):
        """Test that multiple tasks get sequential IDs."""
        task1 = task_service.add_task("Task 1")
        task2 = task_service.add_task("Task 2")
        task3 = task_service.add_task("Task 3")
        assert task1.id == 1
        assert task2.id == 2
        assert task3.id == 3

    def test_add_task_trims_whitespace(self, task_service):
        """Test that add_task trims leading/trailing whitespace."""
        task = task_service.add_task("  Trimmed task  ")
        assert task.description == "Trimmed task"

    def test_add_task_empty_description_raises(self, task_service):
        """Test that empty description raises ValueError."""
        with pytest.raises(ValueError):
            task_service.add_task("")

    def test_add_task_whitespace_only_raises(self, task_service):
        """Test that whitespace-only description raises ValueError."""
        with pytest.raises(ValueError):
            task_service.add_task("   ")


class TestTaskServiceGetAllTasks:
    """Tests for TaskService.get_all_tasks()."""

    def test_get_all_tasks_empty(self, task_service):
        """Test get_all_tasks returns empty list when no tasks."""
        tasks = task_service.get_all_tasks()
        assert tasks == []

    def test_get_all_tasks_returns_sorted_list(self, task_service):
        """Test that get_all_tasks returns tasks sorted by ID."""
        task_service.add_task("Second")
        task_service.add_task("First")
        task_service.add_task("Third")
        tasks = task_service.get_all_tasks()
        assert len(tasks) == 3
        assert tasks[0].id == 1
        assert tasks[1].id == 2
        assert tasks[2].id == 3

    def test_get_all_tasks_returns_task_objects(self, task_service):
        """Test that get_all_tasks returns Task objects."""
        task_service.add_task("Task 1")
        tasks = task_service.get_all_tasks()
        assert all(isinstance(t, Task) for t in tasks)


class TestTaskServiceUpdateTask:
    """Tests for TaskService.update_task()."""

    def test_update_task_description(self, task_service):
        """Test updating task description."""
        task_service.add_task("Original")
        result = task_service.update_task(1, "Updated")
        assert result is not None
        assert result.description == "Updated"

    def test_update_task_returns_none_for_nonexistent(self, task_service):
        """Test that update_task returns None for non-existent ID."""
        result = task_service.update_task(999, "New description")
        assert result is None

    def test_update_task_empty_raises(self, task_service):
        """Test that empty description raises ValueError."""
        task_service.add_task("Task")
        with pytest.raises(ValueError):
            task_service.update_task(1, "")

    def test_update_task_trims_whitespace(self, task_service):
        """Test that update_task trims whitespace."""
        task_service.add_task("Original")
        task_service.update_task(1, "  Updated  ")
        assert task_service._task_store[1].description == "Updated"


class TestTaskServiceDeleteTask:
    """Tests for TaskService.delete_task()."""

    def test_delete_task_returns_true(self, task_service):
        """Test that delete_task returns True for existing task."""
        task_service.add_task("To delete")
        result = task_service.delete_task(1)
        assert result is True

    def test_delete_task_removes_from_store(self, task_service):
        """Test that delete_task removes task from store."""
        task_service.add_task("To delete")
        task_service.delete_task(1)
        assert 1 not in task_service._task_store

    def test_delete_task_returns_false_for_nonexistent(self, task_service):
        """Test that delete_task returns False for non-existent ID."""
        result = task_service.delete_task(999)
        assert result is False

    def test_delete_task_does_not_affect_others(self, task_service):
        """Test that deleting one task doesn't affect others."""
        task_service.add_task("Task 1")
        task_service.add_task("Task 2")
        task_service.add_task("Task 3")
        task_service.delete_task(2)
        assert len(task_service._task_store) == 2
        assert 1 in task_service._task_store
        assert 3 in task_service._task_store


class TestTaskServiceMarkComplete:
    """Tests for TaskService.mark_complete()."""

    def test_mark_complete_changes_status(self, task_service):
        """Test that mark_complete sets status to True."""
        task_service.add_task("Task")
        result = task_service.mark_complete(1)
        assert result is not None
        assert result.status is True

    def test_mark_complete_returns_none_for_nonexistent(self, task_service):
        """Test that mark_complete returns None for non-existent ID."""
        result = task_service.mark_complete(999)
        assert result is None


class TestTaskServiceMarkIncomplete:
    """Tests for TaskService.mark_incomplete()."""

    def test_mark_incomplete_changes_status(self, task_service):
        """Test that mark_incomplete sets status to False."""
        task = task_service.add_task("Task")
        task_service.mark_complete(1)  # First mark complete
        result = task_service.mark_incomplete(1)
        assert result is not None
        assert result.status is False

    def test_mark_incomplete_returns_none_for_nonexistent(self, task_service):
        """Test that mark_incomplete returns None for non-existent ID."""
        result = task_service.mark_incomplete(999)
        assert result is None


class TestTaskServiceIdGeneration:
    """Tests for TaskService ID generation."""

    def test_first_id_is_one(self, task_service):
        """Test that the first task ID is 1."""
        task = task_service.add_task("First task")
        assert task.id == 1

    def test_ids_never_reused_after_deletion(self, task_service):
        """Test that deleted task IDs are not reused."""
        task_service.add_task("Task 1")
        task_service.add_task("Task 2")
        task_service.delete_task(1)
        new_task = task_service.add_task("New task")
        assert new_task.id == 3  # Should be 3, not 1
