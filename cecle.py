import random

i=7
ran=1
while (ran!=0) and (i<=14):
    print("Можна спати далі", i , " година")
    i+=1
    ran=random.randint(0,10)
    if ran==0:
        print("Треба вставати!!!", i, " година")
