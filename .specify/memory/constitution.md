<!--
Sync Impact Report:
- Version change: 1.0.0 → 1.0.0 (initial creation)
- Modified principles: All principles added as new
- Added sections: All sections added as new
- Removed sections: None
- Templates requiring updates:
  - .specify/templates/plan-template.md ✅ updated
  - .specify/templates/spec-template.md ✅ updated
  - .specify/templates/tasks-template.md ✅ updated
  - .specify/templates/commands/*.md ⚠ pending
- Follow-up TODOs: None
-->

# Todo Console Application Constitution

## Core Principles

### I. Spec-First Development
Every feature and change must be specified before implementation. Clear requirements and acceptance criteria must be defined before any code is written. This ensures alignment between business needs and technical implementation.

### II. Clean Architecture
Maintain clear separation of concerns with distinct layers: presentation, business logic, and data access. Business logic must be independent of frameworks and external concerns. Dependencies flow inward from outer layers to core business logic.

### III. Type Safety (NON-NEGOTIABLE)
All Python code must use type hints as defined in PEP 484. Static type checking with mypy or similar tools must pass before merging. Variables, function parameters, return types, and class attributes must be explicitly typed.

### IV. Documentation-First
Every function, class, and module must have comprehensive docstrings following PEP 257. API documentation must be clear and complete. Code should be self-explanatory with meaningful variable and function names.

### V. Minimal Functionality Scope
Only implement the 5 core Todo features: Add, Delete, Update, View, Toggle Complete. No additional features or complexity beyond these basic operations. Focus on doing these few things exceptionally well.

### VI. Maximum Function Length Constraint
No function should exceed 30 lines of code. Complex logic must be broken down into smaller, composable functions. This improves testability, readability, and maintainability.

## Technology and Architecture Constraints

The application must be built using Python 3.13+ with UV package manager. In-memory storage only - no external databases or persistence mechanisms. Prefer standard library over third-party dependencies. Application must run as a console/CLI application with text-based user interface.

## Code Quality and Development Standards

All code must follow PEP 8 style guidelines. SOLID principles must be applied where appropriate. Functions should follow single responsibility principle. Error handling must be graceful with appropriate exception handling and user-friendly error messages. Unit tests must cover all business logic with minimum 80% code coverage.

## Governance

This constitution supersedes all other development practices. All pull requests and code reviews must verify compliance with these principles. Any deviation must be explicitly justified and approved. New features or architectural changes that conflict with these principles require constitution amendments.

**Version**: 1.0.0 | **Ratified**: 2025-12-28 | **Last Amended**: 2025-12-28
