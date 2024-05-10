import sys

class Task:
    pass

class TaskTracker:
    pass
def main():
    manager = TaskManager("tasks.xlsx")

    while True:
        print("\nTask Manager Menu:")
        print("1. Add Task")
        print("2. Display Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter task title: ")
            manager.add_task(title)
        elif choice == "2":
            manager.display_tasks()
        elif choice == "3":
            task_number = int(input("Enter the task number to mark as done: "))
            time_taken = int(input("Enter the time taken for the task in minutes: "))
            manager.mark_task_done(task_number, time_taken)
        elif choice == "4":
            task_number = int(input("Enter the task number to delete: "))
            manager.delete_task(task_number)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
