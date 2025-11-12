import math
""""Порівняння двох гіпотенуз:"""
def hypotenuse(a, b):
    return math.sqrt(a**2 + b**2)

a1 = float(input("Катет а1: "))
b1 = float(input("Катет b1: "))
a2 = float(input("Катет а2: "))
b2 = float(input("Катет b2: "))

h1 = hypotenuse(a1, b1)
h2 = hypotenuse(a2, b2)
print(f"гіпотенуза", round(h1,2), round(h2,2))
if h1 > h2:
    print("Перша більша!")
elif h1 < h2:
    print("Друга більша!")
else:
    print("Рівні!")