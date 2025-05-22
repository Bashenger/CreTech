import json
import datetime
import os

class Task:
    """Represents a single task in the to-do list."""
    def __init__(self, title, description="", due_date_str=None, completed=False):
        if not title:
            raise ValueError("Task title cannot be empty.")

        self.title = title
        self.description = description
        self.creation_date = datetime.datetime.now()
        self.due_date = None
        if due_date_str:
            try:
                self.due_date = datetime.datetime.strptime(due_date_str, "%d-%m-%Y")
            except ValueError:
                print(f"Warning: Due date '{due_date_str}' for task '{title}' is not in DD-MM-YYYY format. No due date set.")
        self.completed = completed

    def __str__(self):
        status_symbol = "[X]" if self.completed else "[ ]"
        due_date_display = self.due_date.strftime("%d-%m-%Y") if self.due_date else "N/A" 
        creation_date_display = self.creation_date.strftime("%d-%m-%Y %H:%M")

        display = f"{status_symbol} {self.title}"
        if self.description:
            display += f"\n    Description: {self.description}"
        display += f"\n    Due: {due_date_display} (Created: {creation_date_display})"
        return display

    def to_dict(self):
        """Converts the Task object into a dictionary for JSON storage."""
        return {
            "title": self.title,
            "description": self.description,
            "creation_date": self.creation_date.isoformat(),
            "due_date": self.due_date.strftime("%d-%m-%Y") if self.due_date else None,
            "completed": self.completed,
        }

    @classmethod
    def from_dict(cls, data_dict):
        """Creates a Task object from a dictionary (e.g., when loading from JSON)."""
        task = cls(
            title=data_dict["title"],
            description=data_dict.get("description", ""),
            due_date_str=None, # Due date is handled from isoformat below
            completed=data_dict.get("completed", False)
        )
        task.creation_date = datetime.datetime.fromisoformat(data_dict["creation_date"])
        if data_dict.get("due_date"):
            task.due_date = datetime.datetime.strptime(data_dict["due_date"], "%d-%m-%Y")
        return task

class TodoList:
    """Manages a collection of tasks and operations."""
    def __init__(self, filename="todolist_data.json"):
        self.tasks = []
        self.filename = filename
        self.load_tasks()

    def add_task(self, title, description="", due_date_str=None):
        try:
            new_task = Task(title, description, due_date_str)
            self.tasks.append(new_task)
            print(f"\nTask '{title}' added successfully.")
            self.save_tasks()
        except ValueError as e:
            print(f"Error adding task: {e}")

    def view_tasks(self, view_filter="all"):
        if not self.tasks:
            print("\nYour to-do list is empty!")
            return

        print("\n--- YOUR TASKS ---")
        tasks_to_show = []
        if view_filter == "pending":
            tasks_to_show = [task for task in self.tasks if not task.completed]
            if not tasks_to_show:
                print("No pending tasks.")
                return
        elif view_filter == "completed":
            tasks_to_show = [task for task in self.tasks if task.completed]
            if not tasks_to_show:
                print("No completed tasks.")
                return
        else: # "all"
            tasks_to_show = self.tasks

        for index, task in enumerate(tasks_to_show):
            print(f"{index + 1}. {task}\n--------------------")

        if not tasks_to_show and view_filter == "all":
             print("\nYour to-do list is empty!")

    def mark_task_status(self, completed_status):
        """Marks a task as completed or pending based on completed_status (True/False)."""
        if not self.tasks:
            print("\nNo tasks to mark.")
            return

        action = "complete" if completed_status else "pending"
        
        # Filter tasks that can actually have their status changed
        if completed_status: # Marking as complete, so list pending tasks
            relevant_tasks = [task for task in self.tasks if not task.completed]
            if not relevant_tasks:
                print(f"\nNo tasks to mark as {action}.")
                return
            print(f"\n--- Select a PENDING task to mark as {action} ---")
        else: # Marking as pending, so list completed tasks
            relevant_tasks = [task for task in self.tasks if task.completed]
            if not relevant_tasks:
                print(f"\nNo tasks to mark as {action}.")
                return
            print(f"\n--- Select a COMPLETED task to mark as {action} ---")

        for index, task in enumerate(relevant_tasks):
            print(f"{index + 1}. {task.title} (Due: {task.due_date.strftime('%d-%m-%Y') if task.due_date else 'N/A'})")
        print("--------------------")

        try:
            task_num_str = input(f"Enter task number to mark as {action}: ")
            task_index_in_relevant_list = int(task_num_str) - 1

            if 0 <= task_index_in_relevant_list < len(relevant_tasks):
                task_to_update = relevant_tasks[task_index_in_relevant_list]
                # Find the task in the main list by object identity to update it
                for original_task in self.tasks:
                    if original_task is task_to_update:
                        if original_task.completed == completed_status:
                            print(f"\nTask '{original_task.title}' is already marked as {action}.")
                        else:
                            original_task.completed = completed_status
                            print(f"\nTask '{original_task.title}' marked as {action}.")
                            self.save_tasks()
                        return # Exit after finding and processing the task
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    def remove_task(self):
        if not self.tasks:
            print("\nNo tasks to remove.")
            return

        print("\n--- Select a task to REMOVE ---")
        self.view_tasks("all") # Show all tasks for selection
        if not self.tasks: # In case view_tasks found nothing (e.g. list became empty)
            return

        try:
            task_num_str = input("Enter task number to remove: ")
            task_index_to_remove = int(task_num_str) - 1 # User sees 1-based index

            if 0 <= task_index_to_remove < len(self.tasks):
                removed_task = self.tasks.pop(task_index_to_remove)
                print(f"\nTask '{removed_task.title}' removed successfully.")
                self.save_tasks()
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    def edit_task(self):
        if not self.tasks:
            print("\nNo tasks to edit.")
            return

        print("\n--- Select a task to EDIT ---")
        self.view_tasks("all")
        if not self.tasks:
            return

        try:
            task_num_str = input("Enter task number to edit: ")
            task_index_to_edit = int(task_num_str) - 1

            if 0 <= task_index_to_edit < len(self.tasks):
                task = self.tasks[task_index_to_edit]
                print(f"\nEditing Task: '{task.title}'")
                print(f"Current Description: {task.description if task.description else 'N/A'}")
                print(f"Current Due Date: {task.due_date.strftime('%d-%m-%Y') if task.due_date else 'N/A'}")

                new_title = input(f"Enter new title (or press Enter to keep '{task.title}'): ").strip()
                new_description = input(f"Enter new description (or press Enter to keep current, type 'clear' to remove): ").strip()
                new_due_date_str = input(f"Enter new due date in DD-MM-YYYY (or press Enter to keep current, type 'clear' to remove): ").strip()

                if new_title:
                    task.title = new_title
                
                if new_description.lower() == 'clear':
                    task.description = ""
                elif new_description:
                    task.description = new_description
                
                if new_due_date_str.lower() == 'clear':
                    task.due_date = None
                elif new_due_date_str:
                    try:
                        task.due_date = datetime.datetime.strptime(new_due_date_str, "%d-%m-%Y")
                    except ValueError:
                        print(f"Warning: New due date '{new_due_date_str}' is not in DD-MM-YYYY format. Due date not changed.")
                
                print(f"\nTask '{task.title}' updated successfully.")
                self.save_tasks()
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    def save_tasks(self):
        """Saves the current list of tasks to the JSON file."""
        tasks_as_dicts = [task.to_dict() for task in self.tasks]
        try:
            with open(self.filename, "w") as f:
                json.dump(tasks_as_dicts, f, indent=4)
        except IOError:
            print(f"Error: Could not save tasks to '{self.filename}'.")

    def load_tasks(self):
        """Loads tasks from the JSON file if it exists."""
        if not os.path.exists(self.filename):
            self.tasks = []
            return

        try:
            with open(self.filename, "r") as f:
                tasks_data = json.load(f)
                self.tasks = [Task.from_dict(task_dict) for task_dict in tasks_data]
        except json.JSONDecodeError:
            print(f"Error: Could not read tasks from '{self.filename}'. File might be corrupted. Starting fresh.")
            self.tasks = []
        except IOError:
            print(f"Error: Could not access tasks file '{self.filename}'.")
            self.tasks = []

# --- Main Application Logic (User Interface) ---

def display_menu():
    print("\n===== TO-DO LIST MENU =====")
    print("1. Add New Task")
    print("2. View All Tasks")
    print("3. View Pending Tasks")
    print("4. View Completed Tasks")
    print("5. Mark Task as Completed")
    print("6. Mark Task as Pending")
    print("7. Edit Task")
    print("8. Remove Task")
    print("0. Exit")
    print("===========================")

def main():
    """Main function to run the To-Do List application."""
    my_todo_list = TodoList()

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            print("\n--- Add New Task ---")
            title = input("Enter task title: ").strip()
            if not title:
                print("Task title cannot be empty. Task not added.")
                continue
            description = input("Enter task description (optional): ").strip()
            due_date_str = input("Enter due date (DD-MM-YYYY, optional, press Enter to skip): ").strip()
            my_todo_list.add_task(title, description, due_date_str)
        elif choice == "2":
            my_todo_list.view_tasks("all")
        elif choice == "3":
            my_todo_list.view_tasks("pending")
        elif choice == "4":
            my_todo_list.view_tasks("completed")
        elif choice == "5":
            my_todo_list.mark_task_status(completed_status=True)
        elif choice == "6":
            my_todo_list.mark_task_status(completed_status=False)
        elif choice == "7":
            my_todo_list.edit_task()
        elif choice == "8":
            my_todo_list.remove_task()
        elif choice == "0":
            print("\nExiting To-Do List. Your tasks are saved. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main()
