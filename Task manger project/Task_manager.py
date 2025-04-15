
'''
overview

project Task manager 

features

1)add a new task
2)view all tasks
3)update a task status
4)delete a task
5)save and load tasks from a file

'''

import json

TASKS_FILE = "tasks.json"

# load tasks from file
def load_tasks():
    try:
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
            if isinstance(data,list): # ensure it's a list
                return data
            else:
                return [] # if the file contains something else, reset  ro empty list
    except (FileNotFoundError, json.JSONDecodeError):
        return []
    
# save tasks to file
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks , file, indent=4)


# add a new task
def add_tasks(tasks):
    title = input("Enter task title : ")
    description = input("Enter task description :  ")
    tasks.append({"title": title, "description": description, "status":"pending"})
    save_tasks(tasks)
    print("✅ Task added sucessfully! ")



#view all tasks

def view_tasks(tasks):
    if not tasks:
        print("No tasks available!")
        return
    print("\n 📌 your tasks: ")
    for idx, task in enumerate(tasks , start=1):
        print(f"{idx}. {task['title']} - {task['description']} [{task['status']}]")


# update a task status
def update_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        task_no = int(input("Enter task number to update:  ")) - 1
        if 0 <= task_no < len(tasks):
            tasks[task_no]["status"] = "completed"
            save_tasks(tasks)
            print("✅  Task updated sucessfully!")
        else:
            print("❌ Invalid task number! ")
    except ValueError:
        print("❌ please enter a valid number! ")


# delete a task

def delete_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        task_no = int(input("Enter task number to delete: ")) - 1
        if 0 <= task_no < len(tasks):
            deleted_task = tasks.pop(task_no)
            save_tasks(tasks)
            print(f" Task  {deleted_task['title']} deleted sucessfully!")
        else:
            print("❌ invalid task number!")
    except ValueError:
        print(" ❌ please enter a valid number! ")
    


# Main menu

def main():
    tasks = load_tasks()
    while True:
        print("\n Task manger ")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. update Task Status")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Enter your choice:  ")

        if choice == "1":
           add_tasks(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            update_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print(" exiting Task Manager. Goodbye!")
            break
        else:
            print("❌ Invalid choice! please enter a number between 1-5.")


#run the program

if __name__ == "__main__":
    main()





