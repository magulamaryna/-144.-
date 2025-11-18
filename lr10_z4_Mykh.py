import random, math

def func(x, y, z, t, angle):
    if angle == 90:
        return f"Площа чотирикутника зі сторонами {x}, {y}, {z}, {t} = {x*y}"
    else:
        return f"Площа чотирикутника зі сторонами {x}, {y}, {z}, {t} = {x*y*math.sin(angle)}"
    
x, y, z, t = map(int, input("Введіть 4 сторони через пробіл: ").split())
angle = random.randint(1, 90)
print(func(x, y, z, t, angle))