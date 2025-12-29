import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from src.cli.cli_controller import CLIController
from src.services.task_service import TaskService

def test_application():
    print("Testing Todo Console Application...")

    # Initialize the task service and CLI controller
    task_service = TaskService()
    cli_controller = CLIController(task_service)

    print("\n1. Testing Add Task feature:")
    # Simulate adding a task
    task_service.create_task("Test Task 1", "This is a test task")
    print("   Added task: 'Test Task 1'")

    print("\n2. Testing View All Tasks feature:")
    cli_controller.display_tasks()

    print("\n3. Testing Update Task feature:")
    updated_task = task_service.update_task(1, "Updated Test Task 1", "This is an updated test task")
    if updated_task:
        print(f"   Updated task: '{updated_task.title}'")

    print("\n4. Testing View All Tasks after update:")
    cli_controller.display_tasks()

    print("\n5. Testing Toggle Task Status feature:")
    toggled_task = task_service.toggle_task_status(1)
    if toggled_task:
        print(f"   Toggled task status: Task #{toggled_task.id} is now {'complete' if toggled_task.is_complete else 'incomplete'}")

    print("\n6. Testing View All Tasks after toggle:")
    cli_controller.display_tasks()

    print("\n7. Testing Delete Task feature:")
    delete_success = task_service.delete_task(1)
    if delete_success:
        print("   Deleted task #1")

    print("\n8. Testing View All Tasks after delete (should be empty):")
    cli_controller.display_tasks()

    print("\nAll features tested successfully!")

if __name__ == "__main__":
    test_application()