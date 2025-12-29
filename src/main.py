from src.cli.cli_controller import CLIController
from src.services.task_service import TaskService


def main():
    """Main application entry point."""
    # Initialize the task service and CLI controller
    task_service = TaskService()
    cli_controller = CLIController(task_service)

    # Run the application with keyboard interrupt handling
    try:
        cli_controller.run()
    except KeyboardInterrupt:
        print("\n\nGoodbye!")
    except EOFError:
        print("\n\nGoodbye!")


if __name__ == "__main__":
    main()
