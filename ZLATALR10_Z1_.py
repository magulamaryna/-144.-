def plosha(a,b):
    s = a * b
    return s
for i in range(1,3+1):
    print("Прямокутник", i)
    a =float(input("Введіть сторону a"))
    b = float(input("Введіть сторону b"))
    s = plosha(a, b)
    print("Площа=",s)
    print()