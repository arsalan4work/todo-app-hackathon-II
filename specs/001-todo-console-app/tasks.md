# Implementation Tasks: Todo Console Application

**Branch**: `001-todo-console-app` | **Date**: 2025-12-28 | **Spec**: [specs/001-todo-console-app/spec.md](specs/001-todo-console-app/spec.md)

## Summary

Implementation of a Python console-based Todo application with in-memory storage, clean architecture, and full CRUD operations. The application will follow the project constitution requirements for type safety, documentation, and code quality.

## Architecture & Design

### Layered Architecture
- **Presentation Layer**: CLI interface handling user input and output
- **Business Logic Layer**: Task services managing operations and validation
- **Data Layer**: In-memory storage using Python collections

### Components to Implement

1. **Task Model** - Data structure with validation
2. **Task Service** - Business logic for CRUD operations
3. **CLI Controller** - Menu and input handling
4. **Application Entry Point** - Main application flow

## Implementation Tasks

### Phase 1: Core Models and Data Structures

- [ ] **TASK-001**: Create Task model with type hints and validation
  - Implement dataclass with id, title, description, completed fields
  - Add validation for title length (1-100 chars) and description (0-500 chars)
  - Include completion status and creation timestamp
  - Add status symbol property (✓/○) for display

- [ ] **TASK-002**: Create in-memory task storage
  - Implement a repository pattern with dictionary-based storage
  - Support operations: add, get by ID, get all, update, delete
  - Ensure thread-safe operations if needed
  - Include auto-increment ID generation

### Phase 2: Business Logic Layer

- [ ] **TASK-003**: Implement TaskService class
  - Add method: create_task(title, description) -> Task
  - Add method: get_task(task_id) -> Task | None
  - Add method: get_all_tasks() -> List[Task]
  - Add method: update_task(task_id, title=None, description=None) -> Task | None
  - Add method: delete_task(task_id) -> bool
  - Add method: toggle_task_status(task_id) -> Task | None

- [ ] **TASK-004**: Implement input validation
  - Create validation functions for title and description
  - Validate character limits and required fields
  - Return appropriate error messages for invalid inputs

- [ ] **TASK-005**: Implement error handling
  - Create custom exception classes for different error types
  - Handle invalid task IDs gracefully
  - Provide user-friendly error messages

### Phase 3: CLI Interface

- [ ] **TASK-006**: Create CLI controller
  - Implement main menu with numbered options
  - Handle user input and command routing
  - Format and display task information

- [ ] **TASK-007**: Implement "Add Task" functionality
  - Prompt for title (required) and description (optional)
  - Validate inputs before creating task
  - Display success message with task details

- [ ] **TASK-008**: Implement "View All Tasks" functionality
  - Display formatted list of all tasks
  - Show ID, title, status (✓/○), and description preview
  - Handle case when no tasks exist

- [ ] **TASK-009**: Implement "Update Task" functionality
  - Prompt for task ID and new title/description
  - Validate inputs before updating
  - Display success/error messages

- [ ] **TASK-010**: Implement "Delete Task" functionality
  - Prompt for task ID with confirmation
  - Validate task exists before deletion
  - Display appropriate feedback

- [ ] **TASK-011**: Implement "Toggle Task Status" functionality
  - Prompt for task ID
  - Toggle completion status and update task
  - Display confirmation of status change

### Phase 4: Application Integration

- [ ] **TASK-012**: Create main application entry point
  - Initialize task service and CLI controller
  - Implement main loop for menu navigation
  - Handle graceful exit

- [ ] **TASK-013**: Implement application configuration
  - Set up UV package manager configuration
  - Define dependencies in pyproject.toml
  - Configure type checking settings

### Phase 5: Testing

- [ ] **TASK-014**: Write unit tests for Task model
  - Test validation logic
  - Test property accessors
  - Test string representation

- [ ] **TASK-015**: Write unit tests for TaskService
  - Test all CRUD operations
  - Test error conditions
  - Test validation behavior

- [ ] **TASK-016**: Write integration tests
  - Test end-to-end functionality
  - Test CLI interaction flow
  - Test error handling

## Technical Implementation Notes

### Type Safety Requirements
- All functions must have type hints (PEP 484)
- All variables must be explicitly typed
- Static type checking with mypy must pass

### Code Quality Standards
- Maximum 30 lines per function
- Follow PEP 8 style guidelines
- Comprehensive docstrings following PEP 257
- Meaningful variable and function names

### Error Handling Strategy
- Graceful handling of invalid inputs
- User-friendly error messages
- No application crashes on invalid operations
- Clear feedback for all operations

## Dependencies & Setup

- Python 3.13+ required
- UV package manager for dependency management
- Standard library only (no external dependencies for core logic)
- Optional: mypy for type checking, pytest for testing

## Success Criteria

- [ ] All 5 core features (Add, View, Update, Delete, Toggle) functional
- [ ] Input validation working correctly
- [ ] Error handling in place with user-friendly messages
- [ ] Clean architecture with separation of concerns
- [ ] Type safety maintained throughout
- [ ] PEP 8 compliance
- [ ] Tests covering all business logic with 80%+ coverage
- [ ] In-memory storage working correctly
- [ ] Menu-based navigation intuitive and responsive