# === Import Modules ===
import datetime as d
import json

# === Note ===
# For this project, I decided to work with the data from the text files as
# dictionaries. However, when I got to the later parts of having to edit tasks
# and write back to the text files, things got a little complicated.
# I hope my comments make sense and that leaving the text file in json format
# is okay. I really wanted to challenge myself try to work it out independantly,
# so I am looking forward your feedback and advice for the future :)

# === Define Functions ===
ALL_TASKS = []
USERS_INFO = {}


def reg_user():
    '''
    This function asks user to input new credentials to be registered as
    new user. It will loop until a unique username and confirmed matching 
    password is entered
    '''
    print("Enter credentials of new user.")
    while True:
        new_user = input("Enter new username:\n")
        # Check if username already exists - each username must be unique
        if new_user not in USERS_INFO:
            break
        print("Username already exists. Please use another.")

    while True:
        new_pass = input("Enter new password:\n")
        repeat_pass = input("Confirm password: ")
        # I tried looking into password hashing to not store passwords in plain
        # text, but it got really complicated really fast.
        if new_pass == repeat_pass:
            with open("user.txt", "a", encoding = "utf-8") as u_file:
                u_file.write(f"\n{new_user}, {new_pass}")
            break
        print("Passwords do not match. Please try again.")

    return "Registration successful."

# The following function was just to convert the original given tasks.txt file
# in the format I wanted to work with. I uploaded the already changed document
# so as to not repeatedly turn dictionaries into dictionaries every time the
# program restarts after the first time. Therefore, I commented out calling this
# and two other function later in the code
def dict_tasks():
    '''
    This function reads any existing task text file and saves the text 
    content of the tasks in dictionary format for easy manipulation. Appends to
    ALL_TASKS list. Only to be called ONCE along with write_tasks() to be able 
    to use tasks.txt in other functions.
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
    with open("tasks.txt", "w", encoding="utf-8") as f_out:
        for a_task in ALL_TASKS:
            json.dump(a_task, f_out)
            f_out.write("\n")


def read_tasks():
    '''
    Read all tasks from text file in json format to append to ALL_TASKS list
    '''
    with open("tasks.txt", "r", encoding="utf-8") as test_file:
        for line in test_file:
            one_task = json.loads(line)
            if one_task not in ALL_TASKS:
                ALL_TASKS.append(one_task)


def read_users():
    '''
    Reads user.txt file and stores all current users and passwords in USERS_INFO
    in dictionary format.
    '''
    with open("user.txt", "r", encoding = "utf-8") as file:
        for line in file:
            single_line = line.strip()
            single_line = single_line.split(", ")
            if single_line[0] not in USERS_INFO:
                USERS_INFO[single_line[0]] = single_line[1]


# This function also only needs to be called once IF the date format of an existing
# tasks.txt does not conform to YYYY-MM-DD. As I have uploaded the already changed
# tasks.txt file, the calling of this function is commented out.
def convert_dates():
    '''
    Converts any existing date formats in tasks.txt into the same usable format
    for comparison and continuity purposes (YYYY-MM-DD)
    '''
    for d_task in ALL_TASKS:
        try:
            # To convert the time format, turn the original time into a
            # date object with original time format, then manipulate to a string
            # with the desired format specified
            d_task["Due date"] = (d.datetime.strptime(
            d_task["Due date"], "%d %b %Y"
            ).strftime("%Y-%m-%d"))
            # Do the same with assigned dates for continuity
            d_task["Date assigned"] = (d.datetime.strptime(
            d_task["Date assigned"], "%d %b %Y"
            ).strftime("%Y-%m-%d"))
        except ValueError as err:
            print(err)


def date_valid(due_date):
    '''
    Takes date input (YYYY-MM-DD) and returns true if it is valid and not in 
    the past.
    '''
    try:
        current_date = d.datetime.today()
        #YYYY-MM-DD

        due_date_obj = d.datetime.strptime(due_date, "%Y-%m-%d")
        if due_date_obj < current_date:
            print("Error, the due date cannot be in the past!")
        else:
            return True
    except ValueError:
        print("Please enter a valid date.")


def check_overdue(tasks):
    '''
    Returns all tasks with overdue due dates in list format. All dates must be
    in the same format - see convert_dates().
    '''
    overdue = []
    today = d.datetime.today() # current date
    # To compare time, both dates must be converted to identical date objects
    for check_task in tasks:
        d_date_obj = d.datetime.strptime(check_task["Due date"], "%Y-%m-%d")
        if d_date_obj < today:
            overdue.append(check_task)
    return overdue


def add_task():
    '''
    This function will add a new task with input details from the user to
    the external text file in the form of a dictionary or json object
    '''
    print("Please enter the following task information: ")

    while True:
        assigned_user = input("User assigned to task: ")
        # Check if user assigned to task even exists in login database
        if assigned_user in USERS_INFO:
            break
        print("User not registered.")

    task_title = input("Title of task: ")
    description = input("Description of the task: \n")
    complete = "No"

    while True:
        d_date = input("Task due date (YYYY-MM-DD): ")
        # Ensure a valid date is entered in the required format
        if date_valid(d_date):
            break
    current_date = d.datetime.today().strftime("%Y-%m-%d")

    with open("tasks.txt", "a", encoding="utf-8") as file:
        new_task = {
            "Task": task_title,
            "Assigned to": assigned_user,
            "Date assigned": current_date,
            "Due date":d_date,
            "Task complete?":complete,
            "Task description":description
            }
        json.dump(new_task, file)
        file.write("\n")

    return "Task added successfully"


def view_all():
    '''
    Print out all tasks currently in file in readable dictionary format
    '''
    read_tasks()
    for v_task in ALL_TASKS:
        for t_key, t_value in v_task.items():
            print(f"{t_key} : {t_value}")
        print("\n")


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


def edit_task(number, step, user):
    '''
    Takes input number of task, action to perform and current logged-on user to
    edit task info, such as user assigned, completed or due date. Appends changed
    data back to ALL_TASKS dict list.
    '''
    task_list = view_mine(user)
    # Change selected task to complete
    if step == "c":
        task_list[number - 1]["Task complete?"] = "Yes"
    elif step == "au":

        while True:
            new_au = input("Enter the new user assigned to this task:\n")
            # Check if new user assigned exists
            if new_au in USERS_INFO:
                break
            print("Username does not exist. Please check spelling or add user first.")
        task_list[number - 1]["Assigned to"] = new_au
    elif step == "dd":
        while True:
            new_date = input("Please enter new due date (YYYY-MM-DD):\n")
            # Ensure new valid due date
            if date_valid(new_date):
                break
        task_list[number - 1]["Due date"] = new_date
    else:
        print("Error, not a valid option")
    # Re-add changed task to all task list
    for entry in task_list:
        if entry not in ALL_TASKS:
            ALL_TASKS.append(entry)


def generate_reports():
    '''
    Generates task_overview.txt and user_overview.txt files (or overwrites 
    existing) with current info regarding all task statistics.
    '''
    read_tasks()
    read_users()
    # For task_overview.txt:
    total_tasks = len(ALL_TASKS)
    completed = 0
    for c_task in ALL_TASKS:
        if c_task["Task complete?"] == "Yes":
            completed += 1
    overdue = check_overdue(ALL_TASKS)

    with open("task_overview.txt", "w", encoding="utf-8") as t_report_f:
        task_report = ({
            "Total tasks": total_tasks,
            "Total completed": completed,
            "Total incomplete tasks": total_tasks - completed,
            "Total overdue tasks": len(overdue),
            "% incomplete":round((total_tasks - completed)/ total_tasks * 100, 2),
            "% overdue": round(len(overdue)/total_tasks * 100, 2)
        })
        json.dump(task_report, t_report_f)

    # For user_overview.txt:
    total_users = len(USERS_INFO)
    with open("user_overview.txt", "w", encoding="utf-8") as u_report_f:

        json.dump({"Total users": total_users}, u_report_f)
        u_report_f.write("\n")
        json.dump({"Total tasks": total_tasks}, u_report_f)
        u_report_f.write("\n")

        for u in USERS_INFO:
            u_tasks = view_mine(u)
            u_total = len(u_tasks)
            if u_total !=0:
                u_complete = 0
                # Nested loop for each user to loop through all tasks and get
                # individual stats
                for u_task in u_tasks:
                    if u_task["Task complete?"] == "Yes":
                        u_complete += 1
                u_incomplete = u_total - u_complete
                u_overdue = len(check_overdue(u_tasks))
                user_report = {u : {
                "Total user tasks": u_total,
                "% Of total tasks assigned to user": round((u_total/total_tasks * 100), 2),
                "% Tasks completed by user": round((u_complete/u_total * 100), 2),
                "% User tasks incomplete": round((u_incomplete/u_total * 100), 2),
                "% User tasks incomplete and overdue": round((u_overdue/u_total * 100), 2)
                }}
            else:
                # Catch users with no tasks assigned yet
                user_report = {u : "This user has no tasks assigned"}

            json.dump(user_report, u_report_f)
            u_report_f.write("\n")
    print("Report generated")


def gen_task_stats():
    '''
    Reads task_overview.txt (or creates it if it doesn't exist yet) and prints 
    out the information in a user-friendly readable format.
    '''
    while True:
        try:
            with open("task_overview.txt", "r", encoding="utf-8") as t_file:
                file_data = json.load(t_file)
            print("Task Overview:\n")
            for line in file_data:
                print(f"{line} : {file_data[line]}")
            break
        # Generate report if it does not exist yet
        except FileNotFoundError:
            generate_reports()


def gen_user_stats():
    '''
    Reads user_overview.txt (or creates it if it doesn't exist yet) and prints 
    out the information in a user-friendly readable format.
    '''
    while True:
        try:
            with open("user_overview.txt", "r", encoding="utf-8") as u_file:
                print("User Overview:")
                for line in u_file:
                    dicts = json.loads(line)
                    for d_user in dicts:
                        # For the case when a user has no tasks assigned and the
                        # value for user key is not a nested dictionary
                        if not isinstance(dicts[d_user], dict):
                            print(f"\n{d_user} : {dicts[d_user]}")
                            continue
                        print(f"\n{d_user}")
                        for nested_task in dicts[d_user]:
                            print(f"{nested_task} : {dicts[d_user][nested_task]}")
            break
        # Generate report if it does not exist yet
        except FileNotFoundError:
            generate_reports()

# === Program Code ===
# --- Login section ---

# Read user.txt and add all info to dictionary as username:password key-values
read_users()

while True:
    print("Welcome to the TaskManager program! Please enter login details:")
    USER_NAME = input("Username: ")
    pass_word = input("Password: ")

# Check for valid username, then valid password
    if USER_NAME in USERS_INFO:
        if pass_word == USERS_INFO[USER_NAME]:
            print("Login successful.")
            break
        print("Invalid password. Try again")
    else:
        print("Invalid username. Try again.")

# --- Menu Section ---
# To explain line 390-392, see comments on lines 45-49 and 107-109
#dict_tasks()
#convert_dates()
#write_tasks()

# Repeat menu presentation with while loop
while True:
    # Present the menu to the user and
    # make sure that the user input is converted to lower case.
    # Check if user is admin for extra options:
    if USER_NAME == "admin":
        menu = input('''\nSelect one of the following options:
r - register a user
a - add task
va - view all tasks
vm - view my tasks
gr - generate reports
ds - display statistics
e - exit
: ''').lower()
    else:
        menu = input('''Select one of the following options:
a - add task
va - view all tasks
vm - view my tasks
e - exit
: ''').lower()

    # Register a new user
    if menu == "r":

        if USER_NAME == "admin":    # Only valid if user is admin
            print(reg_user())

        # Catch unauthorized user
        else:
            print("You are not authorized. Please request an admin to perform this action.")

    # Add a new task
    elif menu == "a":
        print(add_task())

    # View all tasks
    elif menu == "va":
        try:
            view_all()
        # Catch instance where no file exists yet
        except FileNotFoundError:
            new_task_file = open("tasks.txt", "a", encoding="utf-8")
            new_task_file.close()
            print("No tasks recorded yet. Please add tasks.")

    # View tasks assigned to current user
    elif menu == "vm":
        print(f"\nAll tasks assigned to {USER_NAME}: ")
        try:
            # Enumerate tasks assigned to user
            for count, task in enumerate(view_mine(USER_NAME), 1):
                print(f"\n{count}")
                for key, value in task.items():
                    print(f"{key} : {value}")

            edit = input("Do you want to edit tasks? Enter 'y' or 'n':\n").lower()
            if edit == "n":
                continue
            if edit == "y":
                option = int(input('''
    Select number of task you wish to edit,
    or enter -1 to return to main menu: '''))
                if option == -1:
                    continue
                action = input('''
    Type:
        c - mark task as complete
        au - change assigned user
        dd - change task due date
    ''').lower()

                edit_task(option, action, USER_NAME)
                write_tasks()
            else:
                print("Error, not a valid option")
                continue
        # Catch instance where no file exists yet
        except FileNotFoundError:
            new_task_file = open("tasks.txt", "a", encoding="utf-8")
            new_task_file.close()
            print("No tasks recorded yet. Please add tasks.")

    # Generate reports - admin user only:
    elif menu == "gr":
        if USER_NAME == "admin":
            generate_reports()

    # Statistics menu for admin user only:
    elif menu == "ds":
        if USER_NAME == "admin":
            option = input('''
    Type:
            t - display task statistics
            u - display user statistics\n''')
            if option == "t":
                gen_task_stats()
            elif option == "u":
                gen_user_stats()
            else:
                # Catch invalid entries
                print("Error, not a valid option")

    elif menu == "e":
        print("Goodbye!!!")
        exit()
    else:
        print("You have entered an invalid input. Please try again")
