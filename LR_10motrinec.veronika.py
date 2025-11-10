#1
import math
import random


def distace(x1,y1,x2,y2):
    suma = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    print(suma)
    return suma
distace(0,6,8,4)


def trukytnuk_abc(a,b,c):
    p=a+b+c/2
    s=math.sqrt(p*(p-a)+(p-b)+(p-c))
    print(s)
    return s
trukytnuk_abc(1,29,3)


