from Project_2_classes import Task, PersonalTask, WorkTask, TaskManager
from datetime import datetime

def create_personal_task():
 while True:
    try:
        title = input("Enter a task title: ")
        description = input("Enter a task description: ")
        task_manager=TaskManager
        due_date = task_manager._validate_date_input("Enter a task due date (DD/MM/YYYY): ")
        status = input("Enter a task status (Incomplete/Complete/In Progress): ")
        category = input("Enter a task category (Family/Sport...): ")

        return PersonalTask(title, description, due_date, status, category)
    except ValueError:
        print("Invalid input. Please try again.")
def create_work_task():
 while True:
    try:
        title = input("Enter a task title: ")
        description = input("Enter a task description: ")
        task_manager=TaskManager
        due_date = task_manager._validate_date_input("Enter a task due date (DD/MM/YYYY): ")
        status = input("Enter a task status (Incomplete/Complete/In Progress): ")
        priority = input("Enter a task priority (High/Medium/Low): ")


        return WorkTask(title, description, due_date, status, priority)
    except ValueError:
        print("Invalid input. Please try again.")

#C:\Users\hanyo\OneDrive\Desktop\Project
def main():
    task_manager = TaskManager("tasks.json")

    while True:
        print("******************** Welcome to Task Manager System ********************")
        print("[1] Add a task")
        print("[2] Delete a task")
        print("[3] Show list of tasks")
        print("[4] Update task")
        print("[5] Mark task as completed")
        print("[6] Quit")

        choice = input("Please enter your choice: ")

        if choice == "1":
            while True:
                print("[1] Personal Task")
                print("[2] Work Task")

                task_type = input("Please enter the task type: ")

                if task_type == "1":
                    try:
                        task = create_personal_task()
                        task_manager.add_task(task)
                        print("Personal task added successfully.")
                        break
                    except ValueError:
                        print("Invalid input. Please try again.")
                elif task_type == "2":
                    try:
                        task = create_work_task()
                        task_manager.add_task(task)
                        print("Work task added successfully.")
                        break
                    except ValueError:
                        print("Invalid input. Please try again.")
                else:
                    print("Invalid task type. Please enter '1' for Personal Task or '2' for Work Task.")

        elif choice == "2":
            while True:
                title = input("Enter the title of the task you want to delete: ")
                if task_manager.delete_task(title):
                    break
                else:
                    continue

        elif choice == "3":

            task_manager.show_tasks()

        elif choice == "4":

            while True:
                title = input("Enter the title of the task you want to update: ")

                task_manager.update_task(title)

                break

        elif choice == "5":

            while True:
                title = input("Enter the title of the task you want to mark as completed: ")

                task_manager.mark_task_completed(title)

                break

        elif choice == "6":

            print("Thank you for using the Task Manager System. Goodbye!")
            break

        else:

            print("Invalid choice. Please enter a number from 1 to 6.")


main()