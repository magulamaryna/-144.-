import math

def triangle(k1, k2, k3, k4):
    arr = [k1**2 + k2**2, k3**2 + k4**2]
    return f"Гіпотенуза №1: {round(math.sqrt(arr[0]))}\nГіпотенуза №2: {round(math.sqrt(arr[1]))}\nНайбільша гіпотенуза: {max(arr)}\n Найменша гіпотенуза: {min(arr)}"

k1, k2, k3, k4 = map(int, input('Введіть 4 катета через пробіл: ').split())
print(triangle(k1, k2, k3, k4))