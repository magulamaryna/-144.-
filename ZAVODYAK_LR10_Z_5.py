n = int(input("ведіть n"))
nums = list(map(int, input("ведіть числа через пробіл").split()))

print("числа, що діляться на задні")
for i in range(1, n +1):
    if all(i%x == 0 for x in nums):
        print(i, end=" ")

