#1
import numbers
import random
m = int(input("ведіть зміну"))
k = int(input("ведіть зміну"))
k>=3
k<=10
if k < 3 or k > 10:
    print("k має бути від 3 до 10")
else:
    count = 0
    for _ in range(m):
        number = random.randint(-66,666)
        print(f"{number:5}", end="")
        count += 1
        if count == k:
            print()
    if count != 0:
        print()

#2
n = int(input("n: "))
a = int(input("a: "))
b = int(input("b: "))
for _ in range(n):
    num = random.randint(a,b)
    number.append|(num)
    print(num, end="")
print()
s = 0
for i in numbers:
    if i >0:
        s += i
print("сума",s)
max_i = numbers.index(max(numbers, key=abs))
min_i = numbers.index(min(numbers, key=abs))
start = min (max_i, min_i)+1
end = max(max_i, min_i)
p = 1
for i in range[start, end]:
    p *= i
print(p)




