numbers = input("Введіть числа через пробіл: ")
parts = numbers.split()
fout = open("parity.txt", "w", encoding="utf-8")
for p in parts:
    n = int(p)
    if n % 2 == 0:
        fout.write(str(n) + " - парне\n")
    else:
        fout.write(str(n) + " - непарне\n")
fout.close()