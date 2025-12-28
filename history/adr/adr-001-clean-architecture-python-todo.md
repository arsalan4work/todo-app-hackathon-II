# ADR-001: Clean Architecture for Python Todo Console Application

> **Scope**: Document decision clusters, not individual technology choices. Group related decisions that work together (e.g., "Frontend Stack" not separate ADRs for framework, styling, deployment).

- **Status:** Accepted
- **Date:** 2025-12-28
- **Feature:** 001-todo-console-app
- **Context:** Need to structure the Python Todo console application with clear separation of concerns to maintain code quality, testability, and adherence to project constitution requirements.

<!-- Significance checklist (ALL must be true to justify this ADR)
     1) Impact: Long-term consequence for architecture/platform/security?
     2) Alternatives: Multiple viable options considered with tradeoffs?
     3) Scope: Cross-cutting concern (not an isolated detail)?
     If any are false, prefer capturing as a PHR note instead of an ADR. -->

## Decision

Implement clean architecture pattern with three distinct layers:

- **Presentation Layer**: CLI interface handling user input and output (`src/cli/`)
- **Business Logic Layer**: Task services managing operations and validation (`src/services/`)
- **Data Layer**: In-memory storage using Python collections (`src/models/`)

All components will follow the layered approach with dependencies flowing inward from outer layers to core business logic.

## Consequences

### Positive

- Clear separation of concerns makes code more maintainable
- Easier to write unit tests for business logic without UI dependencies
- Adherence to project constitution requirements for clean architecture
- Independent development and testing of business logic
- Future flexibility to change UI or data storage without affecting core logic

### Negative

- More complex initial setup with additional abstraction layers
- Slightly more files and directories to navigate
- Potentially over-engineered for a simple console application
- Requires more coordination between layers for simple operations

## Alternatives Considered

Alternative A: Monolithic approach with all functionality in a single file
- Why rejected: Would violate constitution requirement for clean architecture and separation of concerns, harder to test and maintain

Alternative B: MVC pattern with models, views, controllers
- Why rejected: Still has clear separation but doesn't emphasize the business logic layer as distinctly as clean architecture does

Alternative C: Direct database approach with ORM models
- Why rejected: Project requires in-memory storage only, and this doesn't address the separation of concerns requirement

## References

- Feature Spec: specs/001-todo-console-app/spec.md
- Implementation Plan: specs/001-todo-console-app/plan.md
- Related ADRs: None
- Evaluator Evidence: Project constitution requires clean architecture with clear separation of concerns