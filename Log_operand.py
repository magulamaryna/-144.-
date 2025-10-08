import math

x = int(input("Введіть значення аргумента X"))
a = int(input("Введіть значення змінної А"))

if x<=-2:
    y = math.sin(x+a)
    print("Y=",round(y,2))
elif (-2<x)or(x<=3):
    y = math.cos((x-3.14)**2)
    print("Y=",round(y,2))
elif (x<3) and (a!=0):
    y = math.atan(math.pow(x/a))
    print("Y=",round(y,2))
elif (x<3) and (a==0):
    print("Y=1")