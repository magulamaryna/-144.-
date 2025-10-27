i = 100
while i >= 10:
    print(i)
    i -= 10

work = True
while work:
    user_input = input("Enter word stop:")
    if user_input == "stop":
        work = False
print("While loop is done")
