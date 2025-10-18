user_count_hobby = int(input("Enter hobby number:"))

i = 0
hobby = []
while i < user_count_hobby:
    text ="Enter hobby:" + str(i + 1) + ":"

    hobby.append(input("Enter hobby:"))

    i += 1

print(hobby)