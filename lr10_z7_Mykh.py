def func():
    def is_prime(x):
        if x < 2:
            return False
        i = 2
        while i * i <= x:
            if x % i == 0:
                return False
            i += 1
        return True

    n = int(input("Введи n: "))
    mode = input("Введи режим: ")

    if mode == "список":
        primes = []
        for num in range(2, n + 1):
            if is_prime(num):
                primes.append(num)
        print(primes)

    elif mode == "кількість":
        count = 0
        for num in range(2, n + 1):
            if is_prime(num):
                count += 1
        print(count)

    else:
        for num in range(2, n + 1):
            if is_prime(num):
                print(num)

func()
