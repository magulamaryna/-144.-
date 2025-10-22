import random

def func(a, b):
    if a >= b:
        return "а має бути більше за b"

    array = list(range(random.randint(1, 100), random.randint(200, 1000)))
    max_num_index = array.index(max(array))
    array_1 = list(range(a, b))

    return f"Кількість елементів списку в діапазоні від {a} до {b}: {len(array_1)}\nСума елементів від максимального числа: {sum(array[max_num_index:])}"

a = int(input("a = "))
b = int(input("b = "))
print(func(a, b))
