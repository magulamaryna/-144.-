M = int(input("ведіть М"))
N = int(input("ведіть N"))

max_k = 0
rezult = []
for num in range(M,N+1):
    k = 0
    for i in range(1, num +1):
        if num % i == 0:
         k += 1
    if k > max_k:
        max_k = k
        rezult = [num]
    elif k == max_k:
        rezult.append(num)

print("найбшльша кількість дільників", max_k)
print("числа", rezult)

