import random

n = int(input("Ввести кількість рядків n - "))
m = int(input("Ввести кількість стовбців m - "))
a = int(input("Ввести значення а - "))
b = int(input("Ввести значення b - "))
matrix = [[random.randint(a, b) for i in range(m)] for j in range(n)]
print("Початкова матриця:")
for e in matrix:
    print(e)
e = int()
if (e // 2) * 2 == e:
    print(e,"Парне")
else:
    print(e,"Непарне")
