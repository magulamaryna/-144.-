import random
def matrica(n):
    m = []
    for i in range (n):
        row = []
        for j in range(n):
            row.append(random.randint(-10,10))
        m.append(row)
    return m
def druk(m):
    for row in m:
        print(row)
def podil(m):
    arrP=[]
    arrN=[]
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m [i][j] > 0:
                arrP.append(m[i][j])
            elif m[i][j] < 0:
                arrN.append(m[i][j])
    return  arrP,arrN
n = int(input("Введіть розмір матриці"))
m = matrica(n)
druk(m)
arrP, arrN = podil(m)
print("Додатні елементи",arrP)
print("Відємні елементи",arrN)
