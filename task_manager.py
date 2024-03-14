# --- Import Modules ---
import datetime as d
import json 

# --- Note ---
# For this project, I decided to work with the data from the text files as 
# dictionaries. However, when I got to the later parts of having to edit tasks
# and write back to the text files, things got a little complicated.
# I hope my comments make sense and that leaving the text file in json format
# is okay. I feel like I bit off a little more than I could chew so I am looking  
# forward your feedback and advice for the future :)

# --- Define Functions ---
ALL_TASKS = []
def reg_user():
    '''
    This function asks user to input new credentials to be registered as
    new user. It will loop until a unique username and confirmed matching 
    password is entered
    '''
    print("Enter credentials of new user.")
    while True:
        new_user = input("Enter new username:\n")
        if new_user not in users_info:
            break
        print("Username already exists. Please use another.")
    
    while True:
        new_pass = input("Enter new password:\n")
        repeat_pass = input("Confirm password: ")

        if new_pass == repeat_pass:
            with open("19 Cap2/user.txt", "a", encoding = "utf-8") as file:
                file.write(f"\n{new_user}, {new_pass}")
            break
        print("Passwords do not match. Please try again.")
        
    return "Registration successful."

def dict_tasks():
    '''
    This function reads any existing task text file and saves the text 
    content of the tasks in dictionary format for easy manipulation. Appends to
    ALL_TASKS list.
    '''
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

def write_tasks():
    '''
    Writes the content of ALL_TASKS back to text file as dictionary objects
    '''
    with open("test1.txt", "w", encoding="utf-8") as f_out:
        for task in ALL_TASKS:
            json.dump(task, f_out)
            f_out.write("\n")

def read_tasks():
    '''
    Read all tasks from text file in json format to append to ALL_TASKS list
    '''
    with open("test1.txt", "r", encoding="utf-8") as test_file:
        for line in test_file:
            one_task = json.loads(line)
            if one_task not in ALL_TASKS:
                ALL_TASKS.append(one_task)

def date_valid(due_date):
    '''
    Takes date input (YYYY-MM-DD) and returns true if it is valid and not in 
    the past.
    '''
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

def add_task():
    '''
    This function will add a new task with input details from the user to
    the external text file in the form of a dictionary or json object
    '''
    print("Please enter the following task information: ")

    while True:
        assigned_user = input("User assigned to task: ")
        if assigned_user in users_info:
            break
        print("User not registered.")

    task_title = input("Title of task: ")
    description = input("Description of the task: \n")
    complete = "No" 

    while True:
        d_date = input("Task due date (YYYY-MM-DD): ")
        if date_valid(d_date):
            break  
    current_date = d.datetime.today().strftime("%Y-%m-%d")

    with open("test.txt", "a", encoding="utf-8") as file:
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
    for task in ALL_TASKS:
        for key, value in task.items():
            print(f"{key} : {value}")
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

def edit_task(number, action, user):
    '''
    Takes input number of task, action to perform and current logged-on user to
    edit task info, such as user assigned, completed or due date. Appends changed
    data back to ALL_TASKS dict list.
    '''
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

# Login section

# Read user.txt and add all info to dictionary as username:password key-values
users_info = {}

with open("user.txt", "r", encoding = "utf-8") as file:

    for line in file:
        single_line = line.strip()
        single_line = single_line.split(", ")
        users_info[single_line[0]] = single_line[1]

#print(users_info)


while True:
    print("Welcome to the TaskManager program! Please enter login details:")
    USER_NAME = input("Username: ")
    pass_word = input("Password: ")

# Check for valid username, then valid password

    if USER_NAME in users_info:
        if pass_word == users_info[USER_NAME]:
            print("Login successful.")
            break
        else:
            print("Invalid password. Try again")
    else: 
        print("Invalid username. Try again.")

# #====Menu Section====
# # Repeat menu presentation with while loop
# while True:
#     # Present the menu to the user and 
#     # make sure that the user input is converted to lower case.
#     # Check if user is admin for special s option:
#     if USER_NAME == "admin":
#         menu = input('''\nSelect one of the following options:
# r - register a user
# a - add task
# va - view all tasks
# vm - view my tasks
# s - view statistics
# e - exit
# : ''').lower()
#     else:
#         menu = input('''Select one of the following options:
# a - add task
# va - view all tasks
# vm - view my tasks
# e - exit
# : ''').lower()

#     # Register a new user
#     if menu == "r":

#         if USER_NAME == "admin":    # Only valid if user is admin
#           print(reg_user())
#           
#         # Catch unauthorized user
#         else:
#             print("You are not authorized. Please request an admin to perform this action.")

#     # Add a new task
#     elif menu == "a":
#           print(add_task())
#     # View all tasks
#     elif menu == "va":

#         view_all()

#     # View tasks assigned to current user
#     elif menu == "vm":
#         print(f"\nAll tasks assigned to {USER_NAME}: ")

#        for count, task in enumerate(view_mine(USER_NAME), 1):
#           print(f"\n{count}")
#           for key, value in task.items():
#               print(f"{key} : {value}")
        
#         edit = input("Do you want to edit tasks? Enter 'y' or 'n':\n").lower()
#         if edit == "y":
#             option = int(input('''
# Select number of task you wish to edit, 
# or enter -1 to return to main menu: '''))
#             if option == -1:
#                 print("exit to main menu")
#             action = input('''
# Type:
#     c - mark task as complete
#     au - change assigned user
#     dd - change task due date
# ''').lower()

#             edit_task(option, action, USER_NAME)
#             write_tasks()
        
#     # Statistics menu for admin user only:
#     elif menu == "s":
#         task_num = 0
#         # Because I'm using the length of usersnames list, it must be recalculated at login if users were added.
#         print("Please note, if you added a new user on this session, please log off and back on to refresh statistics.")

#         with open("tasks.txt", "r", encoding = "utf-8") as file:

#             for line in file:
#                 task_num += 1

#         print(f'''\n
# Total number of tasks:        \t{task_num}
# Total number of users:        \t{len(usernames)}
# ''')

#     elif menu == "e":
#         print("Goodbye!!!")
#         exit()
#     else:
#         print("You have entered an invalid input. Please try again")