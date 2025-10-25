#Завдання 1
import math
n = 24
sum = 0
for i in range(1, n+1):
    sum += (2 - math.sqrt(i)) / (math.sqrt(i))
print(sum)

#Завдання 2
print("Число\Таблиця квадрату числа")
for i in range(1, 11):
    print(f"{i}\{i**2}")