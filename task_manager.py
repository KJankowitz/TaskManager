#=====importing libraries===========
from datetime import date

#====Login Section====

usernames = []
passwords = []

with open("user.txt", "r", encoding = "utf-8") as file:

    for line in file:
        single_line = line.strip()
        single_line = single_line.split(", ")

        usernames.append(single_line[0])
        passwords.append(single_line[1])

while True:
    print("Welcome to the TaskManager program! Please enter login details:")
    USER_NAME = input("Username: ")
    pass_word = input("Password: ")

    if USER_NAME in usernames and pass_word in passwords:
        print("Login successful.")
        break

    # Check for valid username, then valid password
    if USER_NAME not in usernames:
        print("Invalid username. Try again.")
    elif pass_word not in passwords:
        print("Invalid password. Try again")

#====Menu Section====
# Repeat menu presentation with while loop
while True:
    # Present the menu to the user and 
    # make sure that the user input is converted to lower case.

    # Check if user is admin for special s option:
    if USER_NAME == "admin":
        menu = input('''\nSelect one of the following options:
r - register a user
a - add task
va - view all tasks
vm - view my tasks
s - view statistics
e - exit
: ''').lower()
    else:
        menu = input('''Select one of the following options:
r - register a user
a - add task
va - view all tasks
vm - view my tasks
e - exit
: ''').lower()

    # Register a new user
    if menu == "r":

        if USER_NAME == "admin":    # Only valid if user is admin
            print("Enter credentials of new user:")
            new_user = input("Username: ")
            while True:
                new_pass = input("Password: ")
                repeat_pass = input("Confirm password: ")

                if new_pass == repeat_pass:

                    with open("user.txt", "a", encoding = "utf-8") as file:
                        file.write(f"\n{new_user}, {new_pass}")
                    break
                else:
                    print("Passwords do not match. Please retry.")
        # Catch unauthorized user
        else:
            print("You are not authorized. Please request an admin to perform this action.")

    # Add a new task
    elif menu == "a":
        print("Please enter the following task information: ")

        assigned_user = input("User assigned to task: ")
        task_title = input("Title of task: ")
        description = input("Description of the task: \n")
        due_date = input("Task due date (eg 12 Jan 2024): ")
        current_date = date.today()
        # Convert current date to same format in tasks.txt
        today = current_date.strftime("%d %b %Y")
        complete = "No"

        with open("tasks.txt", "a", encoding="utf-8") as file:
            file.write(f"\n{assigned_user}, {task_title}, {description}, {today}, {due_date}, {complete}")

    # View all tasks
    elif menu == "va":

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

    # View tasks assigned to current user
    elif menu == "vm":
        print(f"\nAll tasks assigned to {USER_NAME}: ")

        with open("tasks.txt", "r", encoding="utf-8") as file:
            for line in file:
                one_task = line.strip()
                one_task = one_task.split(", ")
                if USER_NAME == one_task[0]:
                    print(f'''\n
Task:             \t{one_task[1]}
Assigned to:      \t{one_task[0]}
Date assigned:    \t{one_task[3]}
Due date:         \t{one_task[4]}
Task complete?    \t{one_task[5]}
Task description: \t{one_task[2]}
''')

    # Statistics menu for admin user only:
    elif menu == "s":
        task_num = 0
        # Because I'm using the length of usersnames list, it must be recalculated at login if users were added.
        print("Please note, if you added a new user on this session, please log off and back on to refresh statistics.")

        with open("tasks.txt", "r", encoding = "utf-8") as file:

            for line in file:
                task_num += 1

        print(f'''\n
Total number of tasks:        \t{task_num}
Total number of users:        \t{len(usernames)}
''')

    elif menu == "e":
        print("Goodbye!!!")
        exit()

    else:
        print("You have entered an invalid input. Please try again")
