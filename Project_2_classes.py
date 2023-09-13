import json
from datetime import datetime
class Task:
    def __init__(self, title, description, due_date, status):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def __str__(self):
        return f"Title: {self.title}\n" \
               f"Description: {self.description}\n" \
               f"Due Date: {self.due_date}\n" \
               f"Status: {self.status}"

class PersonalTask(Task):
    def __init__(self, title, description, due_date, status, task_category):
        super().__init__(title, description, due_date, status)
        self.task_category = task_category

    def __str__(self):
        return super().__str__() + f"\nCategory: {self.task_category}"

    def get_task_type(self):
        return "Personal"

    def get_task_category(self):
        return self.task_category

class WorkTask(Task):
    def __init__(self, title, description, due_date, status, task_priority):
        super().__init__(title, description, due_date, status)
        self.task_priority = task_priority

    def __str__(self):
        return super().__str__() + f"\nPriority: {self.task_priority}"

    def get_task_type(self):
        return "Work"

    def get_task_priority(self):
        return self.task_priority

class TaskManager:
    def __init__(self, json_file_name):
        self.json_file_name = json_file_name

    def get_tasks(self):
        try:
            with open(self.json_file_name, 'r') as file:
                tasks = json.load(file)
        except FileNotFoundError:
            tasks = []
        return tasks

    def save_tasks(self, tasks):
        with open(self.json_file_name, "w") as file:
            json.dump(tasks, file, indent=2)

    def _validate_date_input(self,enter_date):
        while True:
            try:
                date_str = input(enter_date)
                due_date = datetime.strptime(date_str, "%d/%m/%Y").date()
                return due_date.strftime("%d/%m/%Y")
            except ValueError:
                print("Invalid date format. Please enter in DD/MM/YYYY format.")
    def add_task(self, task):
        tasks = self.get_tasks()
        formatted_task = {
            "title": task.title,
            "description": task.description,
            "due_date": task.due_date,
            "status": task.status,
            "task_type": task.get_task_type()
        }

        if isinstance(task, PersonalTask):
            formatted_task["task_category"] = task.get_task_category()
        elif isinstance(task, WorkTask):
            formatted_task["task_priority"] = task.get_task_priority()

        tasks.append(formatted_task)
        self.save_tasks(tasks)
        self.save_tasks(tasks)

    def delete_task(self, title):
        tasks = self.get_tasks()
        found_task = None

        for task in tasks:
            if task["title"] == title:
                found_task = task
                tasks.remove(task)
                break

        if found_task:
            self.save_tasks(tasks)
            print("Task deleted successfully.")
        else:
            print("No task found with the given title. Please try again.")

        return found_task


    def show_tasks(self):
            tasks = self.get_tasks()
            if tasks:
                for task in tasks:
                    print(Task(task["title"], task["description"], task["due_date"], task["status"]))
                    print()
            else:
                print("No tasks found.")



    def update_task(self, title):
                tasks = self.get_tasks()
                for task in tasks:
                    if task["title"] == title:
                        while True:
                            try:
                                print("[1] Update title")
                                print("[2] Update description")
                                print("[3] Update due date")
                                print("[4] Update status")
                                print("[5] Update category (for personal task)")
                                print("[6] Update priority (for work task)")
                                print("[7] Go back to the main menu")

                                attribute_choice = input("Please enter the attribute you want to update: ")

                                if attribute_choice == "1":
                                    new_title = input("Enter the new title: ")
                                    task["title"] = new_title
                                    print("Title updated successfully.")
                                elif attribute_choice == "2":
                                    new_description = input("Enter the new description: ")
                                    task["description"] = new_description
                                    print("Description updated successfully.")
                                elif attribute_choice == "3":
                                    new_due_date = self._validate_date_input("Enter the new due date (DD/MM/YYYY): ")
                                    task["due_date"] = new_due_date
                                    print("Due date updated successfully.")
                                elif attribute_choice == "4":
                                    new_status = input("Enter the new status (Incomplete/Complete/In Progress): ")
                                    task["status"] = new_status
                                    print("Status updated successfully.")
                                elif attribute_choice == "5" and isinstance(task, PersonalTask):
                                    new_category = input("Enter the new category: ")
                                    task["task_category"] = new_category
                                    print("Category updated successfully.")
                                elif attribute_choice == "6" and isinstance(task, WorkTask):
                                    new_priority = input("Enter the new priority (High/Medium/Low): ")
                                    task["task_priority"] = new_priority
                                    print("Priority updated successfully.")
                                elif attribute_choice == "7":
                                    break  # Go back to the main menu
                                else:
                                    print("Invalid choice. Please enter a number from 1 to 7.")

                                self.save_tasks(tasks)
                                break
                            except ValueError:
                                print("Invalid input. Please try again.")

                        break
                else:
                    print("Task not found. Please enter a valid task name.")


    def mark_task_completed(self, title):
                    tasks = self.get_tasks()
                    for task in tasks:
                        if task["title"] == title:
                            task["status"] = "Complete"
                            self.save_tasks(tasks)
                            print("Task marked as completed successfully.")
                            break
                    else:
                        print("Task not found. Please enter a valid task name.")
