import random
m = int(input("Введіть кількість чисел m:"))
k = int(input("Введіть кількість чисел у ряду k:"))
if k < 3 or k > 10:
    print("k має бути у межах 3 до 10.")
y = 0
for i in range(m):
    num = random.randint(13,399)
    print(f"{num:5}", end="")
    y += 1
    if y == k:
        print()
        y = 0
if y != 0:
    print()
