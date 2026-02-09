"""Unit tests for the Task dataclass."""

import pytest
from todo import Task


class TestTaskDataclass:
    """Tests for Task creation and field access."""

    def test_task_creation_with_all_fields(self):
        """Test creating a task with all fields specified."""
        task = Task(id=1, description="Test task", status=False)
        assert task.id == 1
        assert task.description == "Test task"
        assert task.status is False

    def test_task_creation_default_status(self):
        """Test that status defaults to False."""
        task = Task(id=1, description="Test task")
        assert task.status is False

    def test_task_equality(self):
        """Test that two tasks with same values are equal."""
        task1 = Task(id=1, description="Test task", status=False)
        task2 = Task(id=1, description="Test task", status=False)
        assert task1 == task2

    def test_task_inequality_different_id(self):
        """Test that tasks with different IDs are not equal."""
        task1 = Task(id=1, description="Test task", status=False)
        task2 = Task(id=2, description="Test task", status=False)
        assert task1 != task2

    def test_task_inequality_different_description(self):
        """Test that tasks with different descriptions are not equal."""
        task1 = Task(id=1, description="Task A", status=False)
        task2 = Task(id=1, description="Task B", status=False)
        assert task1 != task2

    def test_task_str_representation(self):
        """Test string representation of Task."""
        task = Task(id=1, description="Test task", status=False)
        str_repr = str(task)
        assert "Task" in str_repr
        assert "1" in str_repr
        assert "Test task" in str_repr

    def test_task_immutable_after_creation(self):
        """Test that task fields can be modified (mutable dataclass)."""
        task = Task(id=1, description="Original", status=False)
        task.description = "Modified"
        task.status = True
        assert task.description == "Modified"
        assert task.status is True

    def test_task_with_completed_status(self):
        """Test task with completed status."""
        task = Task(id=1, description="Done task", status=True)
        assert task.status is True
