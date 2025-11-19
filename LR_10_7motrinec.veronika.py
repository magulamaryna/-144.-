def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return True
    return False
n = int(input("ведіть N"))
primes = [i for i in range(n+1) if is_prime(i)]
print("прості числа",primes)
print("кількість чисел", len(primes))