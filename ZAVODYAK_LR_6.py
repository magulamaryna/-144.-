import math

variant = int(input("Ведіть номер варіанту"))
n = variant + 10
print("n = ", n)
for i in range(1, n+1):
   rezult = 2**(-math.sqrt(i))/math.sqrt(i)
print(rezult)

for rezult in range(1,11):
    print(rezult**2)












