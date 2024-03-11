# Define Functions

def reg_user():
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
     
    
# Read user.txt and add all info to dictionary as username:password key-values
users_info = {}

with open("19 Cap2/user.txt", "r", encoding = "utf-8") as file:

    for line in file:
        single_line = line.strip()
        single_line = single_line.split(", ")
        users_info[single_line[0]] = single_line[1]

print(users_info)      

print(reg_user())
