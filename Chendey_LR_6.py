import math

variant = int(input("Введіть номер вашого варіанта"))
n = variant+10
for i in range(1,n+1):
    i+= 1
    y = math.sqrt(2*(i)/math.sqrt((i)+5)-math.sqrt(i))
print(y)
x_digit = sum(int(digit) for digit in str(n))
print(x_digit)
