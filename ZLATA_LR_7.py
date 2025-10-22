import random
m = int(input("Введіть кількість чисел m:"))
k = int(input("Введіть кількість чисел у рядку k"))
if k < 3 or k > 10:
    print("Помилка k має бути від 3 до 10")
else:
  for i in range(1, m+1):
    num = random.randint(-444,333)
    print(num)
    if i % k ==0:
        print()
