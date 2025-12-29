"""Formatters for the Todo Console Application.

This module provides consistent formatting functions for the application.
"""

def format_success_message(message: str) -> str:
    """Format a success message with consistent styling.

    Args:
        message: The success message to format

    Returns:
        Formatted success message with checkmark
    """
    return f"[SUCCESS] {message}"


def format_error_message(message: str) -> str:
    """Format an error message with consistent styling.

    Args:
        message: The error message to format

    Returns:
        Formatted error message with error indicator
    """
    return f"[ERROR] {message}"


def format_info_message(message: str) -> str:
    """Format an info message with consistent styling.

    Args:
        message: The info message to format

    Returns:
        Formatted info message with info indicator
    """
    return f"[INFO] {message}"


def format_warning_message(message: str) -> str:
    """Format a warning message with consistent styling.

    Args:
        message: The warning message to format

    Returns:
        Formatted warning message with warning indicator
    """
    return f"[WARNING] {message}"


def format_task_status(is_complete: bool) -> str:
    """Format task completion status with visual indicators.

    Args:
        is_complete: Whether the task is complete

    Returns:
        Visual indicator for task status (X for complete, O for incomplete)
    """
    return "X" if is_complete else "O"


def format_menu_header(title: str) -> str:
    """Format a menu header with consistent styling.

    Args:
        title: The menu title to format

    Returns:
        Formatted menu header with borders
    """
    border = "=" * len(title)
    return f"\n{title}\n{border}"


def format_task_list_header() -> str:
    """Format the task list header with consistent styling.

    Returns:
        Formatted task list header with borders
    """
    header = f"{'ID':<4} {'Status':<8} {'Title':<25} {'Description Preview':<20}"
    border = "=" * len(header)
    return f"\n{header}\n{border}"


def format_application_header() -> str:
    """Format the application header with consistent styling.

    Returns:
        Formatted application header
    """
    return "\nTodo Console Application\n" + "="*30