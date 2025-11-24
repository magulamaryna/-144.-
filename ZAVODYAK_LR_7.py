import random
m = int(input("ведіть цілі числа n"))
k = int(input("ведіть цілі числа k"))

if 3<=k<=10:
    print("випадкові числа")
z = 0
for i in range(1, m+1):
    w = random.randint(0, 125)
    print(w)
if z == k:
    print()


import random
n = int(input('ведіть n ='))
a = int(input('ведіть a ='))
b = int(input('ведіть b ='))

x =[]
for i in range(n):
    print(x.append(random.randint(a, b)))

for i in range(n):
    print(x[i], end='')
print()

maxi = x[0]
ind = 0
for i in range(1, n):
    if x[i]>maxi:
        maxi=x[i]
        ind=i
print('максимальний елемент', maxi, ', його індекс 1', ind, sep="")

for i in range(n):
    if x[i]>0:
        ind1 = i
        break
for i in range(n-1,-1, -1):
    if x[i]>0:
        ind2=i
        break
print("індекс першого елементу", ind1)
print("індекс другого елементу", ind2)

suma = 0
for i in range(ind1+ind2):
    suma+=x[i]
print("сума елементів=",suma)
