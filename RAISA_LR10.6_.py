m, n = map(int, input("Введіть M i N: ").split())
def divisors_count(x):
    return len([i for i in range(1, x+1) if x % i == 0])
max_div = 0
num = m
for i in range(m, n + 1):
    d = divisors_count(i)
    if d > max_div:
        max_div = d
        num = i
print(f"Число {num} має {max_div} дільників - найбільше")