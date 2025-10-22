n = int(input())

if n > 0:
    print("Це число натуральне")
    if n % 2 == 0:
        print("Воно парне")
    elif n % 4 == 0:
        print("Воно кратне 4")
    else:
        print("Число не парне і не кратне 4")
else:
    print("Це число не натуральне")