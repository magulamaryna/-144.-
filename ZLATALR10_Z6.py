def dilnuky(num):
    count = 0
    for i in range(1, num+1):
        if num % i ==0:
            count +=1
    return count
m = int(input("Введіть початок інтервалу m"))
n = int(input("Введіть кінець інтервалу"))
max_count = 0
numbers = []
for num in range(m,n+1):
    d = dilnuky(num)
    if d > max_count:
        max_count = d
        numbers = [num]
    elif d == max_count:
        numbers.append(num)

print("\n Найбільша кількість дільників", max_count)
print("Числа з такою кількістю дільників", numbers)