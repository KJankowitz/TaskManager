users_info = {}

with open("user.txt", "r", encoding = "utf-8") as file:

    for line in file:
        single_line = line.strip()
        single_line = single_line.split(", ")
        if single_line[0] not in users_info:
            users_info[single_line[0]] = single_line[1]

print(users_info)
print(len(users_info))