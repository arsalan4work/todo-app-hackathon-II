"""CLI controller for the Todo Console Application.

This module handles the user interface and menu system for the application.
"""
from typing import List

from src.models.task import Task
from src.services.task_service import TaskService
from src.utils.validators import validate_title, validate_description, validate_task_id
from src.utils.formatters import (
    format_success_message,
    format_error_message,
    format_task_status,
    format_application_header,
    format_menu_header,
    format_task_list_header
)


class CLIController:
    """Controller class for handling CLI interactions and display."""

    def __init__(self, task_service: TaskService):
        """Initialize the CLI controller with a task service.

        Args:
            task_service: The task service to interact with
        """
        self.task_service = task_service

    def display_tasks(self) -> None:
        """Display all tasks in a formatted table with status indicators."""
        tasks = self.task_service.get_all_tasks()

        if not tasks:
            print("\nNo tasks yet! Add your first task to get started.")
            return

        print("\n" + "="*60)
        print(format_task_list_header())

        for task in tasks:
            status = format_task_status(task.is_complete)
            title = task.title_stripped[:23] + "..." if len(task.title_stripped) > 23 else task.title_stripped
            description = task.description_preview[:18] + "..." if len(task.description_preview) > 18 else task.description_preview

            print(f"{task.id:<4} {status:<8} {title:<25} {description:<20}")

        print("="*60)

    def display_menu(self) -> None:
        """Display the main menu with available options."""
        print(format_application_header())
        print("1. View All Tasks")
        print("2. Add Task")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Toggle Task Status")
        print("6. Exit")
        print("="*30)

    def get_user_choice(self) -> str:
        """Prompt user for menu choice.

        Returns:
            The user's menu choice as a string
        """
        return input("\nEnter your choice (1-6): ").strip()

    def add_task(self) -> None:
        """Prompt user for task details, validate inputs, and create a new task."""
        print("\n--- Add New Task ---")

        # Get title from user
        title = input("Enter task title: ").strip()

        # Validate title
        is_valid, error_msg = validate_title(title)
        if not is_valid:
            print(format_error_message(error_msg))
            return

        # Get description from user (optional)
        description = input("Enter task description (optional): ")

        # Validate description
        is_valid, error_msg = validate_description(description)
        if not is_valid:
            print(format_error_message(error_msg))
            return

        # Create the task
        try:
            task = self.task_service.create_task(title, description)
            print(format_success_message(f"Task #{task.id} '{task.title_stripped}' added!"))
        except ValueError as e:
            print(format_error_message(str(e)))

    def update_task(self) -> None:
        """Prompt user for task ID, validate it exists, then update title and/or description."""
        print("\n--- Update Task ---")

        # Get all tasks to check available IDs
        all_tasks = self.task_service.get_all_tasks()
        available_ids = [task.id for task in all_tasks]

        if not available_ids:
            print(format_error_message("No tasks available to update."))
            return

        # Prompt for task ID
        task_id_str = input(f"Enter task ID to update (Available IDs: {', '.join(map(str, sorted(available_ids)))}): ").strip()

        # Validate task ID
        is_valid, error_msg = validate_task_id(task_id_str, available_ids)
        if not is_valid:
            print(format_error_message(error_msg))
            return

        task_id = int(task_id_str)

        # Get the task to update
        task = self.task_service.get_task(task_id)
        if not task:
            print(format_error_message(f"Task #{task_id} not found."))
            return

        # Display current task details
        print(f"\nCurrent task details:")
        print(f"  ID: {task.id}")
        print(f"  Title: {task.title}")
        print(f"  Description: {task.description}")
        print(f"  Status: {'Completed' if task.is_complete else 'Incomplete'}")

        # Prompt for new title (press Enter to keep existing)
        new_title_input = input(f"\nEnter new title (press Enter to keep '{task.title}'): ")
        new_title = new_title_input if new_title_input.strip() else task.title

        # Validate new title if it was changed
        if new_title != task.title:
            is_valid, error_msg = validate_title(new_title)
            if not is_valid:
                print(format_error_message(error_msg))
                return

        # Prompt for new description (press Enter to keep existing)
        new_description_input = input(f"Enter new description (press Enter to keep '{task.description}'): ")
        new_description = new_description_input if new_description_input else task.description

        # Validate new description if it was changed
        if new_description != task.description:
            is_valid, error_msg = validate_description(new_description)
            if not is_valid:
                print(format_error_message(error_msg))
                return

        # Update the task
        try:
            updated_task = self.task_service.update_task(task_id, new_title, new_description)
            if updated_task:
                print(format_success_message(f"Task #{updated_task.id} '{updated_task.title_stripped}' updated!"))
            else:
                print(format_error_message(f"Failed to update task #{task_id}"))
        except ValueError as e:
            print(format_error_message(str(e)))

    def delete_task(self) -> None:
        """Prompt user for task ID, validate it exists, confirm deletion, then delete the task."""
        print("\n--- Delete Task ---")

        # Get all tasks to check available IDs
        all_tasks = self.task_service.get_all_tasks()
        available_ids = [task.id for task in all_tasks]

        if not available_ids:
            print(format_error_message("No tasks to delete. The list is empty."))
            return

        # Prompt for task ID
        task_id_str = input(f"Enter task ID to delete (Available IDs: {', '.join(map(str, sorted(available_ids)))}): ").strip()

        # Validate task ID
        is_valid, error_msg = validate_task_id(task_id_str, available_ids)
        if not is_valid:
            print(format_error_message(error_msg))
            return

        task_id = int(task_id_str)

        # Get the task to delete
        task = self.task_service.get_task(task_id)
        if not task:
            print(format_error_message(f"Task #{task_id} not found."))
            return

        # Display task details for confirmation
        print(f"\nTask to delete:")
        print(f"  ID: {task.id}")
        print(f"  Title: {task.title}")
        print(f"  Description: {task.description}")
        print(f"  Status: {'Completed' if task.is_complete else 'Incomplete'}")

        # Prompt for confirmation
        confirmation = input(f"\nAre you sure you want to delete this task? (yes/no): ").strip().lower()

        # Check confirmation
        if confirmation in ["yes", "y"]:
            # Delete the task
            success = self.task_service.delete_task(task_id)
            if success:
                print(format_success_message(f"Task #{task_id} deleted."))
            else:
                print(format_error_message(f"Failed to delete task #{task_id}"))
        else:
            print(f"\nDeletion cancelled.")

    def toggle_task_status(self) -> None:
        """Prompt user for task ID, validate it exists, then toggle the completion status."""
        print("\n--- Toggle Task Status ---")

        # Get all tasks to check available IDs
        all_tasks = self.task_service.get_all_tasks()
        available_ids = [task.id for task in all_tasks]

        if not available_ids:
            print(format_error_message("No tasks available to toggle."))
            return

        # Prompt for task ID
        task_id_str = input(f"Enter task ID to toggle status (Available IDs: {', '.join(map(str, sorted(available_ids)))}): ").strip()

        # Validate task ID
        is_valid, error_msg = validate_task_id(task_id_str, available_ids)
        if not is_valid:
            print(format_error_message(error_msg))
            return

        task_id = int(task_id_str)

        # Toggle the task status
        updated_task = self.task_service.toggle_task_status(task_id)
        if updated_task:
            status_text = "complete" if updated_task.is_complete else "incomplete"
            print(format_success_message(f"Task #{updated_task.id} marked as {status_text}"))
        else:
            print(format_error_message(f"Failed to toggle status for task #{task_id}"))

    def run(self) -> None:
        """Run the main application loop."""
        while True:
            self.display_menu()
            choice = self.get_user_choice()

            if choice == "1":
                self.display_tasks()
            elif choice == "2":
                self.add_task()
            elif choice == "3":
                self.update_task()
            elif choice == "4":
                self.delete_task()
            elif choice == "5":
                self.toggle_task_status()
            elif choice == "6":
                print("\nGoodbye!")
                break
            else:
                print(format_error_message(f"Invalid choice '{choice}'. Please enter a number between 1-6."))