import sys

class Task:
    pass
class TaskTracker:

        def save_tasks(self):
            """
            save tasks into an excel file
            """
            wb = openpyxl.Workbook()
            ws = wb.active
            ws.append(["Task", "Status", "Time Taken", "Finish Time"])
            for task in self.tasks:
            ws.append([task.title, task.status, task.time_taken, task.finish_time])
            wb.save(self.file_name)

    
        def load_tasks(self):
            """
            load tasks from an excel file
            """
        try:
            wb = openpyxl.load_workbook(self.file_name)
            ws = wb.active
            tasks = []
            for row in ws.iter_rows(values_only=True):
                title = row[0]
                status = row[1]
                time_taken = row[2]
                finish_time = row[3]
                tasks.append(Task(title, status, time_taken, finish_time))
            wb.close()
            return tasks
        except FileNotFoundError:
            return []
            

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
            pass

        elif choice == '5':
            pass

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
