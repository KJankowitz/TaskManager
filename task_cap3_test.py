# generate reports
import json
import datetime as d

def dict_tasks():
    '''
    This function reads any existing task text file and saves the text 
    content of the tasks in dictionary format for easy manipulation. Appends to
    ALL_TASKS list.
    '''
    with open("tasks.txt", "r", encoding="utf-8") as t_file:
        for task_line in t_file:
            one_task = task_line.strip()
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

def write_tasks():
    '''
    Writes the content of ALL_TASKS back to text file as dictionary objects
    '''
    with open("test.txt", "w", encoding="utf-8") as f_out:
        for task in ALL_TASKS:
            json.dump(task, f_out)
            f_out.write("\n")


def read_tasks():
    '''
    Read all tasks from text file in json format to append to ALL_TASKS list
    '''
    with open("test.txt", "r", encoding="utf-8") as test_file:
        for line in test_file:
            one_task = json.loads(line)
            if one_task not in ALL_TASKS:
                ALL_TASKS.append(one_task)

def convert_dates():
    read_tasks()
    for task in ALL_TASKS:
        try:
            task["Due date"] = (d.datetime.strptime(
            task["Due date"], "%d %b %Y"
            ).strftime("%Y-%m-%d"))
        except ValueError:
            continue

        
USERS_INFO = {}
ALL_TASKS = []

def check_overdue(all_tasks):
    overdue = []
    today = d.datetime.today()
    convert_dates()
    for task in all_tasks:
        d_date_obj = d.datetime.strptime(task["Due date"], "%Y-%m-%d")
        if d_date_obj > today:
            overdue.append(task)
    return overdue

def read_users():
    with open("user.txt", "r", encoding = "utf-8") as file:
        for line in file:
            single_line = line.strip()
            single_line = single_line.split(", ")
            if single_line[0] not in USERS_INFO:
                USERS_INFO[single_line[0]] = single_line[1]

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


def generate_report():
    read_tasks()
    read_users()
    total_tasks = len(ALL_TASKS)
    completed = 0
    for task in ALL_TASKS:
        if task["Task complete?"] == "Yes":
            completed += 1


    with open("task_overview.txt", "w", encoding="utf-8") as t_report:
        task_report = ({
            "Total tasks": total_tasks,
            "Total completed": completed,
            "Total incomplete tasks": total_tasks - completed,
            "Total overdue tasks": len(check_overdue(ALL_TASKS)),
            "% incomplete":(total_tasks - completed)/ total_tasks * 100,
            "% overdue": len(check_overdue(ALL_TASKS))/total_tasks * 100
        })
        json.dump(task_report, t_report)
    
    total_users = len(USERS_INFO)
    with open("user_overview.txt", "w", encoding="utf-8") as u_report:
        for u in USERS_INFO:
            u_total = len(view_mine(u))
            u_complete = 0
            #for u_task in u_total:

        user_report = ({
            "Total users": total_users,
            "Total tasks": total_tasks,
        #     user: [total tasks, complete, incomplete, %, overdue]
        #     "
         })
        json.dump(user_report, u_report)

    print("Report generated")

generate_report()
write_tasks()
read_users()
print(USERS_INFO)

#with open("users_overview.txt", "w", encoding="utf-8") as u_report:
    # Total users from user_info dict
    # Total tasks - global var?
    # for each user : -Total tasks assigned, complete vs incomplete and overdue(%)


