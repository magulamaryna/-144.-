import random
n = int(input("Введіть число n: "))
k = int(input("Введіть число k ( 3 <= k <= 10): "))
numbers = [random.randint(-11, 111) for i in range(k)]
print("Згенеровані числа:", numbers)
