# View Mine
import json

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


    

def edit_task(number, action, user):
    task_list = view_mine(user)
    if action == "c":
        task_list[number - 1]["Task complete?"] = "Yes"
    elif action == "au":
        new_au = input("Enter the new user assigned to this task:\n")

    
    for entry in task_list:
        if entry not in ALL_TASKS:
            ALL_TASKS.append(entry)


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

number = int(input('''
Select number of task you wish to edit, 
or enter -1 to return to main menu: '''))
action = input('''
Type:
    c - mark task as complete
    au - change assigned user
    dd - change task due date
''').lower()


if number == -1:
    print("exit to main menu")

edit_task(number, action, user)
write_tasks()