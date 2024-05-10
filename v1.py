import sys

class Task:
    pass

class TaskTracker:
    def list_tasks(self):
    i = 1
       print("---------------------------------------------------------")
    for each_task in self.tasks:
        print(i,each_task.name)
        print('----Description:',each_task.description)
        if i-1 in self.dict:
            print("Status:",self.dict[i-1]["Status"])
        else :
            print("Status:","Incomplete")
        i+=1
    print("---------------------------------------------------------")

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
            pass

        elif choice == '4':
            task_tracker.list_tasks()

        elif choice == '5':
            pass
        
        elif choice == '6':
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()