#=====importing libraries===========
'''This is the section where you will import libraries'''

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
    user_name = input("Username: ")
    pass_word = input("Password: ")

    if user_name in usernames and pass_word in passwords:
        print("Login successful.")
        break
    
    if user_name not in usernames:
        print("Invalid username. Try again.")
    elif pass_word not in passwords:
        print("Invalid password. Try again")

while True:
    # Present the menu to the user and 
    # make sure that the user input is converted to lower case.
    menu = input('''Select one of the following options:
r - register a user
a - add task
va - view all tasks
vm - view my tasks
e - exit
: ''').lower()

    if menu == 'r':
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

    elif menu == 'a':
        pass
        '''This code block will allow a user to add a new task to task.txt file
        - You can use these steps:
            - Prompt a user for the following: 
                - the username of the person whom the task is assigned to,
                - the title of the task,
                - the description of the task, and 
                - the due date of the task.
            - Then, get the current date.
            - Add the data to the file task.txt
            - Remember to include 'No' to indicate that the task is not complete.'''

    elif menu == 'va':
    
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

    elif menu == 'vm':
        pass
        '''This code block will read the task from task.txt file and
         print to the console in the format of Output 2 presented in the PDF
         You can do it in this way:
            - Read a line from the file
            - Split the line where there is comma and space.
            - Check if the username of the person logged in is the same as the 
              username you have read from the file.
            - If they are the same you print the task in the format of Output 2
              shown in the PDF '''

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have entered an invalid input. Please try again")