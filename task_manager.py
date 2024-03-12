# Import Modules
import datetime as d

# Define Functions

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

def add_task():
    print("Please enter the following task information: ")

    while True:
        assigned_user = input("User assigned to task: ")
        if assigned_user in users_info:
            break
        print("User not registered.")

    task_title = input("Title of task: ")
    description = input("Description of the task: \n")
    
    while True:
        try:
            due_date = input("Task due date (YYYY-MM-DD): ")
            current_date = d.datetime.today()
        #YYYY-MM-DD
            today = current_date.strftime("%Y-%m-%d")

            due_date_obj = d.datetime.strptime(due_date, "%Y-%m-%d")
            if due_date_obj > current_date:
                break
            print("Error, the due date cannot be in the past!")
        except ValueError:
            print("Please enter a valid date.")      
    complete = "No"

    with open("tasks.txt", "a", encoding="utf-8") as file:
        file.write(f"\n{assigned_user}, "
                f"{task_title}, "
                f"{description}, "
                f"{today}, "
                f"{due_date}, "
                f"{complete}"
                )
    return "Task added successfully"

def view_all():
    with open("tasks.txt", "r", encoding="utf-8") as file:
                for line in file:
                    one_task = line.strip()
                    one_task = one_task.split(", ")
                    print(f'''\n
    Task:             \t{one_task[1]}
    Assigned to:      \t{one_task[0]}
    Date assigned:    \t{one_task[3]}
    Due date:         \t{one_task[4]}
    Task complete?    \t{one_task[5]}
    Task description: \t{one_task[2]}
    ''')
                    
def view_mine(user):
    with open("tasks.txt", "r", encoding="utf-8") as file:
                for line in file:
                    one_task = line.strip()
                    one_task = one_task.split(", ")
                    if user == one_task[0]:
                    print(f'''\n
    Task:             \t{one_task[1]}
    Assigned to:      \t{one_task[0]}
    Date assigned:    \t{one_task[3]}
    Due date:         \t{one_task[4]}
    Task complete?    \t{one_task[5]}
    Task description: \t{one_task[2]}
    ''')


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

#        view_mine(USER_NAME)
        
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