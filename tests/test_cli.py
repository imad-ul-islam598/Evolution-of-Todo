"""Integration tests for the CLI interface."""

import pytest
from io import StringIO

from todo import CLI, Task, TaskService


class TestCLIHandleView:
    """Tests for CLI._handle_view()."""

    def test_view_empty_list_shows_message(self, cli_with_service, capsys):
        """Test that viewing an empty list shows appropriate message."""
        cli_with_service._handle_view()
        captured = capsys.readouterr()
        assert "No tasks yet" in captured.out

    def test_view_shows_tasks_with_status(self, task_service, capsys):
        """Test that view shows tasks with correct status indicators."""
        cli = CLI(task_service)
        task_service.add_task("Task 1")
        task_service.add_task("Task 2")
        task_service.mark_complete(1)
        cli._handle_view()
        captured = capsys.readouterr()
        assert "[ ]" in captured.out
        assert "[X]" in captured.out
        assert "Task 1" in captured.out
        assert "Task 2" in captured.out

    def test_view_shows_task_ids(self, task_service, capsys):
        """Test that view shows task IDs."""
        cli = CLI(task_service)
        task_service.add_task("First task")
        task_service.add_task("Second task")
        cli._handle_view()
        captured = capsys.readouterr()
        assert "1." in captured.out
        assert "2." in captured.out


class TestCLIHandleAdd:
    """Tests for CLI._handle_add()."""

    def test_add_task_success(self, cli_with_service, capsys, monkeypatch):
        """Test successful task addition."""
        monkeypatch.setattr("builtins.input", lambda _: "New task")
        cli_with_service._handle_add()
        captured = capsys.readouterr()
        assert "Task added" in captured.out

    def test_add_empty_description_error(self, cli_with_service, capsys, monkeypatch):
        """Test that empty description shows error."""
        monkeypatch.setattr("builtins.input", lambda _: "")
        cli_with_service._handle_add()
        captured = capsys.readouterr()
        assert "Error" in captured.out
        assert "empty" in captured.out.lower()


class TestCLIHandleUpdate:
    """Tests for CLI._handle_update()."""

    def test_update_task_success(self, task_service, capsys, monkeypatch):
        """Test successful task update."""
        cli = CLI(task_service)
        task_service.add_task("Original")
        # First input is task ID, second is new description
        monkeypatch.setattr("builtins.input", lambda prompt: "1" if "ID" in prompt else "Updated")
        cli._handle_update()
        captured = capsys.readouterr()
        assert "updated" in captured.out.lower()

    def test_update_invalid_id_error(self, task_service, capsys, monkeypatch):
        """Test that invalid ID shows error."""
        cli = CLI(task_service)
        task_service.add_task("Task")
        monkeypatch.setattr("builtins.input", lambda prompt: "999" if "ID" in prompt else "New")
        cli._handle_update()
        captured = capsys.readouterr()
        assert "Error" in captured.out
        assert "999" in captured.out


class TestCLIHandleDelete:
    """Tests for CLI._handle_delete()."""

    def test_delete_task_success(self, task_service, capsys, monkeypatch):
        """Test successful task deletion."""
        cli = CLI(task_service)
        task_service.add_task("To delete")
        monkeypatch.setattr("builtins.input", lambda prompt: "1")
        cli._handle_delete()
        captured = capsys.readouterr()
        assert "deleted" in captured.out.lower()

    def test_delete_invalid_id_error(self, task_service, capsys, monkeypatch):
        """Test that invalid ID shows error."""
        cli = CLI(task_service)
        task_service.add_task("Task")
        monkeypatch.setattr("builtins.input", lambda prompt: "999")
        cli._handle_delete()
        captured = capsys.readouterr()
        assert "Error" in captured.out


class TestCLIHandleToggle:
    """Tests for CLI._handle_toggle()."""

    def test_mark_complete_success(self, task_service, capsys, monkeypatch):
        """Test marking task as complete."""
        cli = CLI(task_service)
        task_service.add_task("Task")
        monkeypatch.setattr("builtins.input", lambda prompt: "1")
        cli._handle_toggle(complete=True)
        captured = capsys.readouterr()
        assert "complete" in captured.out.lower()

    def test_mark_incomplete_success(self, task_service, capsys, monkeypatch):
        """Test marking task as incomplete."""
        cli = CLI(task_service)
        task = task_service.add_task("Task")
        task_service.mark_complete(1)  # First mark complete
        monkeypatch.setattr("builtins.input", lambda prompt: "1")
        cli._handle_toggle(complete=False)
        captured = capsys.readouterr()
        assert "incomplete" in captured.out.lower()

    def test_toggle_invalid_id_error(self, task_service, capsys, monkeypatch):
        """Test that invalid ID shows error."""
        cli = CLI(task_service)
        task_service.add_task("Task")
        monkeypatch.setattr("builtins.input", lambda prompt: "999")
        cli._handle_toggle(complete=True)
        captured = capsys.readouterr()
        assert "Error" in captured.out


class TestCLIGetValidTaskId:
    """Tests for CLI._get_valid_task_id()."""

    def test_get_valid_task_id_success(self, cli_with_service, monkeypatch):
        """Test getting a valid task ID."""
        monkeypatch.setattr("builtins.input", lambda prompt: "1")
        result = cli_with_service._get_valid_task_id("Enter ID: ")
        assert result == 1

    def test_get_valid_task_id_empty_input(self, cli_with_service, monkeypatch):
        """Test that empty input returns None."""
        monkeypatch.setattr("builtins.input", lambda prompt: "")
        result = cli_with_service._get_valid_task_id("Enter ID: ")
        assert result is None

    def test_get_valid_task_id_invalid_number(self, cli_with_service, capsys, monkeypatch):
        """Test that non-numeric input shows error."""
        inputs = iter(["abc", "1"])
        monkeypatch.setattr("builtins.input", lambda prompt: next(inputs))
        result = cli_with_service._get_valid_task_id("Enter ID: ")
        captured = capsys.readouterr()
        assert "valid number" in captured.out.lower()
        assert result == 1

    def test_get_valid_task_id_negative_number(self, cli_with_service, capsys, monkeypatch):
        """Test that negative number shows error."""
        inputs = iter(["-1", "1"])
        monkeypatch.setattr("builtins.input", lambda prompt: next(inputs))
        result = cli_with_service._get_valid_task_id("Enter ID: ")
        captured = capsys.readouterr()
        assert "positive" in captured.out.lower()
        assert result == 1


class TestCLIDisplayMenu:
    """Tests for CLI._display_menu()."""

    def test_display_menu_shows_options(self, cli_with_service, capsys):
        """Test that menu displays all options."""
        cli_with_service._display_menu()
        captured = capsys.readouterr()
        assert "Add Task" in captured.out
        assert "View Tasks" in captured.out
        assert "Update Task" in captured.out
        assert "Delete Task" in captured.out
        assert "Mark Complete" in captured.out
        assert "Mark Incomplete" in captured.out
        assert "Exit" in captured.out


class TestCLIGetMenuChoice:
    """Tests for CLI._get_menu_choice()."""

    def test_get_menu_choice_valid(self, cli_with_service, monkeypatch):
        """Test getting a valid menu choice."""
        monkeypatch.setattr("builtins.input", lambda prompt: "1")
        result = cli_with_service._get_menu_choice()
        assert result == "1"

    def test_get_menu_choice_invalid_then_valid(self, cli_with_service, capsys, monkeypatch):
        """Test that invalid choices are rejected."""
        inputs = iter(["abc", "0", "5"])
        monkeypatch.setattr("builtins.input", lambda prompt: next(inputs))
        result = cli_with_service._get_menu_choice()
        captured = capsys.readouterr()
        assert "Invalid choice" in captured.out
        assert result == "5"
