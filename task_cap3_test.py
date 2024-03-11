# Login feature

# Read user.txt and add all info to dictionary as username:password key-values
users_info = {}

with open("user.txt", "r", encoding = "utf-8") as file:

    for line in file:
        single_line = line.strip()
        single_line = single_line.split(", ")
        users_info[single_line[0]] = single_line[1]

print(users_info)


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