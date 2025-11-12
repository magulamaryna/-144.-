import math
a, b, r = map(float, input("Введіть f, b, r: ").split())
points = [(1, 2), (3, 4), (5, 6)]
for (x, y ) in points:
    if (x - a)**2 + (y - b)**2 < r**2:
        print(f"Точка ({x}, {y}) - всередині кола")
    elif (x - a)**2 + (y - b)**2 == r**2:
        print(f"Точка ({x}, {y}) - на колі")
    else:
        print(f"Точка ({x}, {y}) - поза колом")