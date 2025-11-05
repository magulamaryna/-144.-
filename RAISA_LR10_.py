#Завдання 1
def zminna1(a, b):
    a = a+b
    b = a-2*b
    return a, b
print("Програма буде змінювати значення двох дійсних змінних.")
a = float(input("Введіть число a: "))
b = float(input("Введіть число b: "))
a1, b1 = zminna1(a, b)
print("Після зміни:")
print("a=", a1)
print("b=", b1)

#Завдання 2
import random
def create_matrix(n):
    matrix = []
    for i in range(n):
        row = [random.randint(1, 9) for _ in range(n)]
        matrix.append(row)
    return matrix
def find_min_in_row(matrix, row):
    return min(matrix[row])
def shift_row_left(matrix, row, k):
    k = k % len(matrix[row])
    matrix[row] = matrix[row][k:] + matrix[row][k:]
n = int(input("Введіть розмір матриці: "))
matrix = create_matrix(n)
print("Початкова матриця: ")
for r in matrix:
    print(r)
row = int(input("Введіть номер рядка для зсуву: "))
k = find_min_in_row(matrix, row)
shift_row_left(matrix, row, k)
print("\nМатриця після зсуву: ")
for r in matrix:
    print(r)