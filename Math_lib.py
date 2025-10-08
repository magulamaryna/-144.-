import math

print("Давай я провірю твої знання з математики, помчали...")
x1 = int(input("ВВедіть значення х1 ="))
y1 = math.sqrt(math.pow(x1,2)+5*x1+8)
print("Y1=", round(y1,1))

x2 = int(input("ВВедіть значення х2 ="))
y2 = (3*(x2**2)-4)/(x2+2)
print("Y2=", round(y2,1))

x3 = int(input("Введіть x3"))
y3 = x3 - math.sqrt(x3+2)
print("y3=", round(y3,1))


