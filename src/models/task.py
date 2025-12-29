"""Task data model for the Todo Console Application.

This module defines the Task dataclass with validation and status indicators.
"""
from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Task:
    """Represents a todo task with validation and status tracking."""

    id: int
    title: str
    description: str = ""
    is_complete: bool = False
    created_at: datetime = None

    def __post_init__(self):
        """Validate task attributes after initialization."""
        if self.created_at is None:
            self.created_at = datetime.now()

        # Validate title
        if not isinstance(self.title, str):
            raise ValueError("Title must be a string")
        if len(self.title.strip()) < 1:
            raise ValueError("Title cannot be empty")
        if len(self.title.strip()) > 100:
            raise ValueError("Title cannot exceed 100 characters")

        # Validate description
        if not isinstance(self.description, str):
            raise ValueError("Description must be a string")
        if len(self.description) > 500:
            raise ValueError("Description cannot exceed 500 characters")

        # Validate other fields
        if not isinstance(self.id, int) or self.id < 0:
            raise ValueError("ID must be a non-negative integer")
        if not isinstance(self.is_complete, bool):
            raise ValueError("is_complete must be a boolean")

    @property
    def status_symbol(self) -> str:
        """Return the status symbol for display (X for complete, O for incomplete)."""
        return "X" if self.is_complete else "O"

    @property
    def title_stripped(self) -> str:
        """Return the stripped title."""
        return self.title.strip()

    @property
    def description_preview(self) -> str:
        """Return a preview of the description (truncated to 50 chars if needed)."""
        if len(self.description) <= 50:
            return self.description
        return self.description[:47] + "..."