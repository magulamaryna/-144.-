import random

def func(a, b, r, points):
    point = 0
    for x, y in points:
        if (x-a)**2 + (y-b)**2 <= r**2:
            point += 1
    return f"Точок всередині кола: {point}"

a, b, r = map(int, input("Введіть координати центру кола та радіус: ").split())
points = [(random.randint(0, 100), random.randint(0, 100)) for _ in range(10)]
print(func(a, b, r, points))