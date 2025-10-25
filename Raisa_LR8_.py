n = int(input("Введіть кількість рядків: "))
m = int(input("Введіть кількість стовпців: "))
a = int(input("Мінімальне значення: "))
b = int(input("Максимальне значення: "))
A = []
import random
for i in range(n):
    row = []
    for j in range(m):
        row.append(random.randint(a, b))
    A.append(row)
sum_cols = [0] * m
for j in range(m):
    for i in range(n):
        sum_cols[j] += A[i][j]
print("Матриця:")
for row in A:
    print(row)
print('Сума стовпців:', sum_cols)