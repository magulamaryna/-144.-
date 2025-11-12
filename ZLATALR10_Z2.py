import math
def hipotenyza (a,b):
    return math.sqrt(a**2 + b**2)
print("Перший трикутник")
a1=float(input("Введіть перший катет a1"))
b1 = float(input("Введіть другий катет b1"))
c1 = hipotenyza(a1, b1)
print("Гіпотенуза першогого трикутника=",c1)
print("\n Другий трикутник")
a2 = float (input("Введіть перший катет a2"))
b2 = float(input("Введть другий катет,b2"))
c2 = hipotenyza(a2,b2)
print("Гіпотенуза другого трикутника",c2)
print()
if c1 > c2:
    print("Гіпотенуза першого трикутника більша")
elif c2 > c1:
    print("Гіпотенуза другого трикутника більша")
else:
    print("Гіпотенузи рівні")
