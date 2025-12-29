"""Task service for the Todo Console Application.

This module provides business logic for task operations with in-memory storage.
"""
from datetime import datetime
from typing import List, Optional

from src.models.task import Task


class TaskService:
    """Service class for managing task operations with in-memory storage."""

    def __init__(self):
        """Initialize the task service with an empty in-memory storage."""
        self._tasks: dict[int, Task] = {}
        self._next_id: int = 1

    def create_task(self, title: str, description: str = "") -> Task:
        """Create a new task with validation and auto-assigned ID.

        Args:
            title: The task title (1-100 characters)
            description: Optional task description (0-500 characters)

        Returns:
            The created Task object

        Raises:
            ValueError: If title or description validation fails
        """
        # Create task with auto-assigned ID
        task = Task(
            id=self._next_id,
            title=title,
            description=description,
            is_complete=False,
            created_at=datetime.now(),
        )

        # Store the task
        self._tasks[task.id] = task
        self._next_id += 1

        return task

    def get_task(self, task_id: int) -> Optional[Task]:
        """Get a task by its ID.

        Args:
            task_id: The ID of the task to retrieve

        Returns:
            The Task object if found, None otherwise
        """
        return self._tasks.get(task_id)

    def get_all_tasks(self) -> List[Task]:
        """Get all tasks in the system.

        Returns:
            A list of all Task objects, sorted by ID
        """
        return sorted(self._tasks.values(), key=lambda task: task.id)

    def update_task(
        self, task_id: int, title: Optional[str] = None, description: Optional[str] = None
    ) -> Optional[Task]:
        """Update a task's title and/or description.

        Args:
            task_id: The ID of the task to update
            title: New title (optional)
            description: New description (optional)

        Returns:
            The updated Task object if successful, None if task doesn't exist
        """
        if task_id not in self._tasks:
            return None

        task = self._tasks[task_id]

        # Update title if provided
        if title is not None:
            # Re-create task to trigger validation
            updated_task = Task(
                id=task.id,
                title=title,
                description=task.description,
                is_complete=task.is_complete,
                created_at=task.created_at,
            )
            task.title = updated_task.title

        # Update description if provided
        if description is not None:
            # Re-create task to trigger validation
            updated_task = Task(
                id=task.id,
                title=task.title,
                description=description,
                is_complete=task.is_complete,
                created_at=task.created_at,
            )
            task.description = updated_task.description

        return task

    def delete_task(self, task_id: int) -> bool:
        """Delete a task by its ID.

        Args:
            task_id: The ID of the task to delete

        Returns:
            True if the task was deleted, False if it didn't exist
        """
        if task_id not in self._tasks:
            return False

        del self._tasks[task_id]
        return True

    def toggle_task_status(self, task_id: int) -> Optional[Task]:
        """Toggle the completion status of a task.

        Args:
            task_id: The ID of the task to toggle

        Returns:
            The updated Task object if successful, None if task doesn't exist
        """
        if task_id not in self._tasks:
            return None

        task = self._tasks[task_id]
        task.is_complete = not task.is_complete
        return task

    @property
    def next_id(self) -> int:
        """Get the next available ID for a new task."""
        return self._next_id