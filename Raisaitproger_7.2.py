user_count_baby = int(input("Enter baby number: "))

i = 0
hobby = []
while i < user_count_baby:
    TEXT = "Enter hobby" + str(i + 1) + ": "
    hobby.append(input(TEXT))

    i += 1
print(hobby)