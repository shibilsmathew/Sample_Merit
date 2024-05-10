import sys
import datetime

class Task:
    def __init__(self, name, description):
        self.name = name
        self.description = description

class TaskTracker:

    def task_schedule(self):

        self.list_tasks()
        task_select = int(input("Enter the task you want to schedule: "))
        user_status = input("Enter your progress (Incompleted / In progress / Completed): ")
        minutes = int(input("Enter end task time (minutes): "))

        current_time = datetime.datetime.now()
        future_time = current_time + datetime.timedelta(minutes=minutes)

        self.dict[task_select-1] = {"Status":user_status,
                                    "Completion_time":future_time}
        
    def list_tasks_with_schedule(self):
        self.list_tasks()
        task_select = int(input("Enter the task you want to refer: "))
        if task_select-1 in self.dict:
            print('--',self.tasks[task_select-1].name)
            print("Status:",self.dict[task_select-1]["Status"])
            print("Expected Task Completion date and time:",self.dict[task_select-1]["Completion_time"])
        else:
            print("No schedule has been provided for this task")

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
            task_tracker.task_schedule()

        elif choice == "3":
            pass
        elif choice == "4":
            pass

        elif choice == '5':
            task_tracker.list_tasks_with_schedule()

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
