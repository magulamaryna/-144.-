import math
def hipotenyza(a,b):
    return math.sqrt(a**2 + b**2)
a1 = float(input("катет а1 = "))
b1 = float(input("катет b1 = "))
a2 = float(input("катет а2 = "))
b2 = float(input("катет b2 = "))

h1 = hipotenyza(a1,b1)
h2 = hipotenyza(a2,b2)

print("гіпотенуза 1 =" , round(h1,2), "гіпотенуза 2 = ", round(h2,2))

if h1>h2:
    print("перша гіпотенуза бiльша.")
if h2>h1:
    print("друга гіпотенуза бiльша.")
else:
    print("гіпотенузи рівні")