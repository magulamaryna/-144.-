import random

arr_1 = []
arr_2 = []
result = []

for i in range(1, 11):
    arr_1.append(random.randint(1, 100))

for i in range(1, 11):
    arr_2.append(random.randint(1, 100))
    if len(arr_2) == 10:
        break

for i in range(len(arr_1)):
    result.append(arr_1[i] * arr_2[i])

print(result)