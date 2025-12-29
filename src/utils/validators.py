"""Input validators for the Todo Console Application.

This module provides validation functions for task title and description inputs.
"""
from typing import Tuple


def validate_title(title: str) -> Tuple[bool, str]:
    """Validate task title according to requirements.

    Args:
        title: The title to validate

    Returns:
        Tuple of (is_valid, error_message)
    """
    # Check if title is empty or contains only whitespace
    stripped_title = title.strip()
    if not stripped_title:
        return False, "Title cannot be empty or contain only whitespace"

    # Check if title exceeds 100 characters
    if len(stripped_title) > 100:
        return False, f"Title cannot exceed 100 characters (current: {len(stripped_title)})"

    return True, ""


def validate_description(description: str) -> Tuple[bool, str]:
    """Validate task description according to requirements.

    Args:
        description: The description to validate

    Returns:
        Tuple of (is_valid, error_message)
    """
    # Description is optional, so empty strings are valid
    if not description:
        return True, ""

    # Check if description exceeds 500 characters
    if len(description) > 500:
        return False, f"Description cannot exceed 500 characters (current: {len(description)})"

    return True, ""


def validate_task_id(task_id_str: str, available_ids: list) -> Tuple[bool, str]:
    """Validate task ID according to requirements.

    Args:
        task_id_str: The task ID string to validate
        available_ids: List of available task IDs

    Returns:
        Tuple of (is_valid, error_message)
    """
    # Check if the input is numeric
    if not task_id_str.isdigit():
        return False, f"Task ID must be a positive number, got: '{task_id_str}'"

    task_id = int(task_id_str)

    # Check if the ID is positive
    if task_id <= 0:
        return False, f"Task ID must be a positive number, got: {task_id}"

    # Check if the ID exists in available IDs
    if task_id not in available_ids:
        ids_str = ", ".join(str(id) for id in sorted(available_ids))
        return False, f"Task #{task_id} not found. Available task IDs: {ids_str}"

    return True, ""