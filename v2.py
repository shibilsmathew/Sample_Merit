import sys

class Task:
    pass

class TaskTracker:
    def task_deletion(self):
        self.list_tasks()
        task_select = int(input("Select the task you want to delete: "))
        try:
            del self.tasks[task_select-1]
            if task_select-1 in self.dict:
                del self.dict[task_select-1]
            a = 0
        except:
            print("Enter a valid input")

def main():

    task_tracker = TaskTracker()

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
            pass

        elif choice == '2':
            pass

        elif choice == '3':
            task_tracker.delete_task(task_number)

        elif choice == '4':
            pass

        elif choice == '5':
            pass

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
