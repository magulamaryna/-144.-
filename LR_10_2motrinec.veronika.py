import math
def katet(a,b):
    hypotenuse=math.sqrt((a**2)+(b**2))
    return hypotenuse
print(katet(65,2))
print(katet(4,3))
print(katet(9,2.5))
spusok = (katet(4,3), katet(9,2.5), katet(65,2))
min(spusok)
print(min(spusok))
max(spusok)
print(max(spusok))