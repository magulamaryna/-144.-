import math
def heron (a,b,c):
    p = (a+b+c)/2
    s = math.sqrt(p*(p - a)* (p - b)*(p - c))
    return s
print("Введіть сторони чотирикутника")
X = float(input("X="))
Y = float(input("Y = "))
Z = float(input("Z="))
T = float(input("T = "))
d = math.sqrt(X**2 + Y**2)
S1 = 0.5 * X * Y
S2 = heron(Z,T,d)
S = S1 + S2
print("\n Площа чотирикутника =",S)