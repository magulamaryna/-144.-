n = 32
n = int(input("Введіть кількість чисел n:"))
numbers =[]
for i in range(n):
    num = float(input("Введіть число"))
    i+1
    numbers.append(num)
max_num = max(numbers)
print("Найбільше число:",max_num)