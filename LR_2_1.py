import math
#x0 = -1.5
xk = 3.5
dx = 0.5
a = -1.25
b = -1.5
c = 0.75
x = -1.5
while x<=xk:
    if x!=0:
        y=(1/(10**2)*b*c)/x + math.sqrt(math.pow(a,3)*x)
        print("Y=", round(y,2))
        x+=dx
    elif x==0:
        print("Помилка, ділення на нуль!")
        break
x=0.5
while x<=xk:
    y=(1/(10**2)*b*c)/x + math.sqrt(math.pow(a,3)*x)
    print("Y=", round(y,2))
    x+=dx



