# View Mine

all_tasks = []
def read_tasks():
    with open("test.txt", "r", encoding="utf-8") as file:
        for line in file:
            one_task = line.strip()
            one_task = one_task.split(", ")
            if one_task not in all_tasks:
                all_tasks.append(one_task)

def view_mine(user):
    my_tasks = []
    read_tasks()
    for task in all_tasks:
        if user == task[0]:
            my_tasks.append(task)
    return my_tasks

print(view_mine("admin"))
# for count, task in enumerate(view_mine("admin"), 1):          
#     print(f'''\n
#     {count}.
#     Task:             \t{task[1]}
#     Assigned to:      \t{task[0]}
#     Date assigned:    \t{task[3]}
#     Due date:         \t{task[4]}
#     Task complete?    \t{task[5]}
#     Task description: \t{task[2]}
#     ''')

             
def edit_task(number, action, user):
    task_list = view_mine(user)
    if action == "c":
        task_list[number - 1][5] = "Yes"
    return task_list

print(edit_task(2, "c", "admin"))
# for entry in edit_task(3, "c", "admin"):
#     if entry not in all_tasks:
#         all_tasks.append(entry)

# print(all_tasks)


# with open("test.txt", "w+", encoding="utf-8") as f_out:
#     for task in all_tasks:
#         task = " ".join(task)
#         f_out.write(task + "\n")
     
