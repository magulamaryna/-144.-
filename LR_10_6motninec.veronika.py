N = int(input(" ведіть число N"))
M = int(input("ведіть число M"))
max_dil = 0
for i in range(M, N+1):
    zmin = 0
    for j in range(1, i+1):
        if i % j == 0:
            zmin += 1
    if zmin > max_dil:
        max_dil = zmin
print("число з найбільшою кількістю дільників",max_dil)


