import random
m = int(input("Введіть кількість рядків (m)"))
n = int(input("Введіть кількість стовпчиків (n)"))
if n < 3:
    print("\n Матриця повинна мати хоча б 3 стовпчики")
a = float(input("Введіть нижню межу a"))
b = float (input("Введіть верхню межу b"))
if b <= a:
    print("\n Верхня межа має бути більшою за нижню \n")
matrix = []
for i in range(m):
    line = []
    for j in range(n):
        num = random.uniform(a,b)
        line.append(num)
    matrix.append(line)
print(" Початкова матриця ")
for i in range(m):
    print()
    for j in range(n):
        print(round(matrix[i][j],2 ), " ", end="")

max_el_3 = matrix[0] [2]
for i in range(1,m):
    if matrix[i][2] > max_el_3:
       max_el_3 = matrix[i][2]
print("\n Максимальний елемент 3 стовпчика \n", round(max_el_3,2))
sum_neparni = 0
for j in range(n):
    if int(matrix[0][j]) % 2 !=0:
        sum_neparni += matrix[0][j]
print("\n Сума непарних елементів першого рядка \n", round(sum_neparni,2))
