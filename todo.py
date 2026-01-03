"""Console Todo Application - Phase I

A simple in-memory todo list application with menu-driven CLI interface.
No databases, files, or external dependencies - Python standard library only.
"""

from dataclasses import dataclass


@dataclass
class Task:
    """Represents a single todo item."""
    id: int
    description: str
    status: bool = False


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


def main() -> None:
    """Application entry point."""
    task_store: dict[int, Task] = {}
    service = TaskService(task_store)
    cli = CLI(service)
    cli.run()


if __name__ == "__main__":
    main()
