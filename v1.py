import sys
import datetime
import openpyxl

class Task:
    def __init__(self,name,description):
        self.name = name
        self.description = description



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
        

    def save_tasks(self):
        """
        save tasks into an excel file
        """
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.append(["Task", "Status", "Finish Time"])
        i = 0
        for task in self.tasks:
            ws.append([task.name, self.dict[i]["Status"], self.dict[i]["Completion_time"]])
            i+=1
        wb.save(self.file_name)   

    def task_deletion(self):
        self.list_tasks()
        task_select = int(input("Select the task you want to delete: "))
        try:
            del self.tasks[task_select-1]
            if task_select-1 in self.dict:
                del self.dict[task_select-1]
        except:
            print("Enter a valid input")

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
            task_tracker.task_deletion()

        elif choice == '4':
            task_tracker.list_tasks()
       
        elif choice == '5':
            task_tracker.list_tasks_with_schedule()
            
        elif choice == '6':
            break

        else:
            print("Invalid choice. Please enter a valid option.")

