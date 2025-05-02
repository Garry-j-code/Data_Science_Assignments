import os
import uuid

def taskIdGenerator():
    return uuid.uuid4().int

def addDataIntoTodoList():
    n = int(input("Please enter how many task's you want to enter into the list: "))
    while(n):
        task_id = str(taskIdGenerator())
        task_id  = "Task Id: " + task_id
        task_name = str(input("\nPlease enter task name: "))
        task_name = "Task Name: " + task_name
        description = str(input("Please enter task description: "))
        description = "Description: " + description
        isTaskCompleted = "Task Status: Not Completed"
       
        taskData = [task_id, task_name, description, isTaskCompleted]

        HERE = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(HERE, "todoListDatabase.text")

        with open(db_path,"a+") as f:
            f.write("\n")
            for item in taskData:
                f.write(f"{item}\n")

        n -= 1

def getAllActiveTask():

    HERE = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(HERE, "todoListDatabase.text")
    users = []
    with open(db_path,"r") as f:
        record = {}
        for line in f:
            line = line.strip()
            if not line:
                if record:
                    users.append(record)
                    record = {}
            else:
                key, value = line.split(": ", 1)
                record[key] = value
        if record:
            users.append(record)
    print()
    for ele in users:
        print()
        for key, value in ele.items():
            print(f"{key}: {value}")

def removeFromTodoList():
    task_id = str(input("\nEnter the task ID which you want want to remove from the list: "))

    HERE = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(HERE, "todoListDatabase.text")
    tasks = []
    with open(db_path,"r") as f:
        record = {}
        for line in f:
            line = line.strip()
            if not line:
                if record:
                    tasks.append(record)
                    record = {}
            else:
                key, value = line.split(": ", 1)
                record[key] = value
        if record:
            tasks.append(record)
    
    filtered_Data = []
    
    for task in tasks:
        if (task["Task Id"] != task_id):
           filtered_Data.append(task)

    with open(db_path,"w") as f:
        f.write("\n")
        for task in filtered_Data:
            for key in task:
                f.write(f"{key}: {task[key]}\n")
            if task != tasks[-1]:
                f.write("\n")

    print(f"The task with task Id: {task_id!r} is removed from the todo List.")

def completeTheTask():
    task_id = str(input("\nEnter the task ID which you want to mark as completed: "))

    HERE = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(HERE, "todoListDatabase.text")
    tasks = []
    with open(db_path,"r") as f:
        record = {}
        for line in f:
            line = line.strip()
            if not line:
                if record:
                    tasks.append(record)
                    record = {}
            else:
                key, value = line.split(": ", 1)
                record[key] = value
        if record:
            tasks.append(record)
    
    filtered_Data = []
    updated = True
    for task in tasks:
        if (task["Task Id"] == task_id):
            updated = False
            task["Task Status"] = "Completed"
            filtered_Data.append(task)
            
        else:
            filtered_Data.append(task)

    if updated:
        print(f"\nThis task {task_id} is not present in the current Database, Please check your input")
        return

    with open(db_path,"w") as f:
        f.write("\n")
        for task in filtered_Data:
            for key in task:
                f.write(f"{key}: {task[key]}\n")
            if task != tasks[-1]:
                f.write("\n")

    print(f"The task with task Id: {task_id!r} marked as completed.")

check = True
while(check):
    print("\nWelcome to my to do list")
    print("Press 1 to add the task to the list")
    print("Press 2 to remove the task from the list")
    print("Press 3 to complete the task")
    print("Press 4 to get all active task")
    print("Press 5 to Close the Program")

    choice = int(input("\nEnter your choice: "))

    if(choice == 1):
        print("\nTask that are already present in the Todo List are as follow: ")
        getAllActiveTask()
        addDataIntoTodoList()
        print("\nOur New Todo list is as follow: ")
        getAllActiveTask()
    elif(choice == 2):
        print("\nTask that are already present in the Todo List are as follow: ")
        getAllActiveTask()
        removeFromTodoList()
        print("\nOur New Todo list is as follow: ")
        getAllActiveTask()
    elif(choice == 3):
        print("\nTask that are already present in the Todo List are as follow: ")
        getAllActiveTask()
        completeTheTask()
        print("\nOur New Todo list is as follow: ")
        getAllActiveTask()
    elif(choice == 4):
        getAllActiveTask()
    elif(choice == 5):
        check = False