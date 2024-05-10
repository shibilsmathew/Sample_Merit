import sys
import datetime
import openpyxl # for working with .xlsx file

class Task:
    '''
    constructor which initializes instances 
    '''
    def __init__(self,name,description):
        self.name = name
        self.description = description



class TaskTracker:
    '''
    stores all the features of the task  management app
    '''
    def list_tasks(self):
        '''
        function: all the tasks are displayed
        returns: list of tasks
        '''
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
        '''
        function: tracks the progress of the task, asks user how much time certain task will take
        returns: current progress of the task
        '''
        self.list_tasks()
        task_select = int(input("Enter the task you want to schedule: "))
        user_status = input("Enter your progress (Incompleted / In progress / Completed): ")
        minutes = int(input("Enter how long the task is going to take (minutes): "))

        current_time = datetime.datetime.now()
        future_time = current_time + datetime.timedelta(minutes=minutes)

        self.dict[task_select-1] = {"Status":user_status,
                                    "Completion_time":future_time}
        
    def list_tasks_with_schedule(self):
        '''
        function: 
        params:
        returns: 
        '''
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
        '''
        function: adds task to the list named 'task'
        params: name and description of the task
        '''
        task = Task(name, description)
        self.tasks.append(task)
        

    def save_tasks(self):
        """
        function: save tasks into an excel file
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
        '''
        function: deletes a certain task from the excel file
        '''
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

        if choice == '1': # for adding tasks
            name = input("Enter task name: ")
            description = input("Enter task description: ")
            task_tracker.add_task(name, description)

        elif choice == '2': # for scheduling tasks
            task_tracker.task_schedule()

        elif choice == "3": # delete tasks
            task_tracker.task_deletion()

        elif choice == '4': # listing/displaying tasks
            task_tracker.list_tasks()
       
        elif choice == '5': # list task with schedule
            task_tracker.list_tasks_with_schedule()
            
        elif choice == '6': # exit
            break

        else:
            print("Invalid choice. Please enter a valid option.")

