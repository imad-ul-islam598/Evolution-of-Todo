"""Pytest configuration and fixtures for Todo Application tests."""

import pytest

from todo import CLI, Task, TaskService


@pytest.fixture
def empty_task_store():
    """Provide an empty task store for tests."""
    return {}


@pytest.fixture
def task_service(empty_task_store):
    """Provide a TaskService with an empty task store."""
    return TaskService(empty_task_store)


@pytest.fixture
def cli_with_service(task_service):
    """Provide a CLI with a TaskService."""
    return CLI(task_service)


@pytest.fixture
def sample_task():
    """Provide a sample Task for testing."""
    return Task(id=1, description="Sample task", status=False)


@pytest.fixture
def task_service_with_tasks(empty_task_store):
    """Provide a TaskService with some pre-added tasks."""
    service = TaskService(empty_task_store)
    service.add_task("Task 1")
    service.add_task("Task 2")
    service.add_task("Task 3")
    return service
