n = int(input("Введіть значення n: "))
nums = list(map(int, input("Введіть дільники: ").split()))
for i in range(1, n + 1):
    if all(i % d == 0 for d in nums):
        print(i, end=" ")