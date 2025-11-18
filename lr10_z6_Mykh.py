nums = []
divs = 0
def func(x):
    count = 0
    i = 1
    while i * i <= x:
        print(i, i*i, x%i)
        if x % i == 0:
            count += 1
        i += 1
    return count

def func2(m, n):
    global nums, divs
    for num in range(m, n + 1):
        d = func(num)
        if d > divs:
            divs = d
            nums = [num]
        elif d == divs:
            nums.append(num)
    return nums

m = int(input("M = "))
n = int(input("N = "))
print(func2(m, n))