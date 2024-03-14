# View Mine
import json
import datetime as d

ALL_TASKS = []
# Turn all Tasks into dict format
def dict_tasks():
    with open("test1.txt", "r", encoding="utf-8") as file:
        for line in file:
            one_task = line.strip()
            one_task = one_task.split(", ")
            one_dict = {
                "Task": one_task[1],
                "Assigned to": one_task[0],
                "Date assigned": one_task[3],
                "Due date":one_task[4],
                "Task complete?":one_task[5],
                "Task description":one_task[2]
            }
            if one_dict not in ALL_TASKS:
                ALL_TASKS.append(one_dict)
            
def read_tasks():
    with open("test1.txt", "r", encoding="utf-8") as test_file:
        for line in test_file:
            one_task = json.loads(line)
            if one_task not in ALL_TASKS:
                ALL_TASKS.append(one_task)

def view_mine(user):
    my_tasks = []
    read_tasks()
    for a_task in ALL_TASKS:
        if user == a_task["Assigned to"]:
            my_tasks.append(a_task)
    return my_tasks


def write_tasks():
    with open("test1.txt", "w", encoding="utf-8") as f_out:
        for task in ALL_TASKS:
            json.dump(task, f_out)
            f_out.write("\n")
     
user = "Tom"

for count, task in enumerate(view_mine(user), 1):
    print(f"\n{count}")
    for key, value in task.items():
        print(f"{key} : {value}")


def date_valid(due_date):
    try:
        current_date = d.datetime.today()
        #YYYY-MM-DD
        today = current_date.strftime("%Y-%m-%d")

        due_date_obj = d.datetime.strptime(due_date, "%Y-%m-%d")
        if due_date_obj < current_date:
            print("Error, the due date cannot be in the past!")
        else:
            return True
    except ValueError:
        print("Please enter a valid date.")

users_info = {
    "admin": "adm1n",
    "John": "j0hn",
    "Frik": "fr1k"
}

def edit_task(number, action, user):
    task_list = view_mine(user)
    if action == "c":
        task_list[number - 1]["Task complete?"] = "Yes"
    elif action == "au":
    
        while True:
            new_au = input("Enter the new user assigned to this task:\n")
            if new_au in users_info:
                break
            print("Username does not exist. Please check spelling or add user first.")
        task_list[number - 1]["Assigned to"] = new_au
    elif action == "dd":
        while True:
            new_date = input("Please enter new due date (YYYY-MM-DD):\n")
            if date_valid(new_date):
                break
        task_list[number - 1]["Due date"] = new_date
                
    for entry in task_list:
        if entry not in ALL_TASKS:
            ALL_TASKS.append(entry)



option = int(input('''
Select number of task you wish to edit, 
or enter -1 to return to main menu: '''))
if option == -1:
    print("exit to main menu")
action = input('''
Type:
    c - mark task as complete
    au - change assigned user
    dd - change task due date
''').lower()

edit_task(option, action, user)
write_tasks()
