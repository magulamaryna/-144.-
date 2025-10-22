import math
n = 32
S = 0
for i in range(1, n+1):
    S = S+1/math.sqrt(i+3)
    print("S=",S)

