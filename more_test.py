import json
import datetime as d
users_info = {}
ALL_TASKS = []

def read_tasks():
    '''
    Read all tasks from text file in json format to append to ALL_TASKS list
    '''
    with open("test.txt", "r", encoding="utf-8") as test_file:
        for line in test_file:
            one_task = json.loads(line)
            if one_task not in ALL_TASKS:
                ALL_TASKS.append(one_task)

def view_mine(user):
    '''
    Returns a list of tasks assigned to current logged-on user in dictionary 
    format. 
    '''
    my_tasks = []
    read_tasks()
    for a_task in ALL_TASKS:
        if user == a_task["Assigned to"]:
            my_tasks.append(a_task)
    return my_tasks

def check_overdue(all_tasks):
    overdue = []
    today = d.datetime.today()
    #convert_dates()
    for task in all_tasks:
        d_date_obj = d.datetime.strptime(task["Due date"], "%Y-%m-%d")
        if d_date_obj > today and task["Task complete?"] == "No":
            overdue.append(task)
    return overdue

with open("user.txt", "r", encoding = "utf-8") as file:

    for line in file:
        single_line = line.strip()
        single_line = single_line.split(", ")
        if single_line[0] not in users_info:
            users_info[single_line[0]] = single_line[1]

#print(users_info)
total_users = len(users_info)
total_tasks =  6


        
report_head = ({
            "Total users": total_users,
            "Total tasks": total_tasks,
            })

for u in users_info:
    u_tasks = view_mine(u)
    if u_tasks == 0:
        u_total
    u_total = len(u_tasks)
    u_complete = 0
    for u_task in u_tasks:
        if u_task["Task complete?"] == "Yes":
            u_complete += 1
    u_overdue = len(check_overdue(u_tasks))
    user_report = [u, {
        "Total user tasks": u_total,
        "% Of total tasks assigned to user": u_total/total_tasks * 100,
        "% Tasks completed by user": u_complete/u_total * 100,
        "% User tasks still incomplete": (u_total - u_complete)/u_total * 100,
        "% User tasks incomplete and overdue": u_overdue/u_total * 100
        }]
    
    print(report_head)
    print(user_report)