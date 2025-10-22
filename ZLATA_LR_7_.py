import random
n = int(input("Кількість елементів n: "))
a = int(input("Початок інтервалу a:"))
b = int(input("Кінець інтервалу b:"))
list = []
for i in range(n):
    list.append(random.randint(a,b))
print("Список",list)
min_el = list[0]
for el  in list:
    if el < min_el:
        min_el = el
print("Мінімальний елемент",min_el)

first = -1
last = -1
for i in range(n):
    if list[i] > 0:
        if first == -1:
            first = i
            last = i

if first == -1:
    print("У списку немає додатніх елементів")
else:
    print("Перший додатній елемент",list[first])
    print("Останній додатний елемент",list[last])
sum1 = 0
if first != -1 and last != -1:
    for i in range(first+1,last):
       sum1 +=list[i]
print("Сума між першим і останнім додатними",sum1)




