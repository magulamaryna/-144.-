def dilitsya_na_vsi(chislo,a,b):
    return (chislo % a == 0) and (chislo % b == 0)
n = int(input("Введіть число n"))
a = int(input("Введіть перше число"))
b = int(input("Введіть другше число"))
print("\n Числа, що не перевищують" ,n ,"і ділиться на", a, "та",b )
for i in range(1, n+1):
    if dilitsya_na_vsi(i,a,b):
        print(i)