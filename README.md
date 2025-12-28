# Todo Console Application

A Python-based command-line todo application with in-memory storage, clean architecture, and full CRUD operations.

## Features

- **Add Tasks**: Create new todo items with title and optional description
- **View Tasks**: Display all tasks with status indicators and descriptions
- **Update Tasks**: Modify existing task details
- **Delete Tasks**: Remove tasks with confirmation prompt
- **Toggle Status**: Mark tasks as complete/incomplete
- **Menu Navigation**: Intuitive numbered menu interface
- **Input Validation**: Comprehensive validation with user-friendly error messages
- **Clean Architecture**: Separation of concerns with models, services, and CLI layers

## Requirements

- Python 3.13+
- UV package manager
- In-memory storage (no external dependencies)

## Architecture

The application follows a clean, layered architecture:

```
┌─────────────────┐
│   Presentation  │  CLI Interface (User Input/Output)
├─────────────────┤
│   Business      │  Task Service (Validation, Logic)
│   Logic         │
├─────────────────┤
│   Data Access   │  In-Memory Repository
└─────────────────┘
```

### Components

- **Task Model**: Data structure with validation and type hints
- **Task Service**: Business logic layer for CRUD operations
- **Repository**: In-memory storage with auto-incrementing IDs
- **CLI Controller**: Menu-driven interface for user interaction

## Project Structure

```
todo-app-hackaton-II/
├── src/
│   ├── models/
│   │   └── task.py          # Task data model with validation
│   ├── services/
│   │   └── task_service.py  # Business logic for task operations
│   └── cli/
│       └── cli_controller.py # Console interface and menu system
├── tests/
│   ├── unit/
│   ├── integration/
│   └── contract/
├── specs/
│   └── 001-todo-console-app/ # Specification documents
└── pyproject.toml            # Project dependencies
```

## Quality Standards

- **Type Safety**: All functions have type hints (PEP 484)
- **Code Quality**: PEP 8 compliance with comprehensive docstrings (PEP 257)
- **Function Length**: Maximum 30 lines per function
- **Clean Architecture**: Clear separation of concerns
- **Testing**: Minimum 80% code coverage with unit and integration tests
- **Error Handling**: Graceful handling with user-friendly messages

## Getting Started

1. Ensure Python 3.13+ is installed
2. Install UV package manager
3. Install project dependencies using `uv sync`
4. Run the application with `python -m src.main`

## Usage

The application provides a menu-driven interface:

1. Add a new task
2. View all tasks
3. Update a task
4. Delete a task
5. Toggle task completion status
6. Exit the application

## Validation

All requirements are verified through the checklist at:
`specs/001-todo-console-app/checklists/requirements.md`

## Specifications

Detailed specifications are available in the `specs/001-todo-console-app/` directory:
- `spec.md` - Feature requirements and user stories
- `plan.md` - Architecture and technical approach
- `tasks.md` - Implementation tasks and checklist
- `complete-spec.md` - Complete consolidated specification

## Development

This project follows Spec-Driven Development (SDD) principles with comprehensive documentation and testing requirements.

### Constitution Compliance

The application strictly follows the project constitution:
- Type safety with PEP 484 type hints
- Clean architecture with separation of concerns
- Maximum 30 lines per function
- In-memory storage only
- Python 3.13+ with UV package manager
- Comprehensive documentation with PEP 257 docstrings
- 80%+ test coverage