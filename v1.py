import sys

class Task:
    def __init__(self, name, description):
        self.name = name
        self.description = description

class TaskTracker:

    def __init__(self):
        self.tasks = []
        self.dict = {}

    def add_task(self, name, description):
        task = Task(name, description)
        self.tasks.append(task)

def main():
    
    task_manager = TaskManager()

if __name__ == "__main__":

    task_tracker = TaskTracker()

    while True:
        print("\nTask Tracker Menu:")
        print("1. Add Task")
        print("2. Schedule Task")
        print("3. Delete Task")
        print("4. List Tasks")
        print("5. List Task with Schedules")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter task name: ")
            description = input("Enter task description: ")
            task_tracker.add_task(name, description)

        elif choice == '2':
            pass
        elif choice == "3":
            pass
        elif choice == "4":
            pass
        elif choice == "5":
            pass
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
