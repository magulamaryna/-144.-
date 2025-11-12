n = int(input("ведіть n"))
a = int(input("ведіть число a "))
b = int(input("ведіть число b"))
for i in range(n):
    if i % a == 0 and i % b == 0:
        print("число що діляться на", a, "i на", b)
        print(i)

