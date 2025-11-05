slovnuk = input("Введіть текстовий рядок: ")
vidkruta_d = slovnuk.count("(")
zakruta_d = slovnuk.count(")")
if vidkruta_d == zakruta_d:
    print("Кількість відкритих і закритих дужок співпадає. ")
else:
    print("Кількість дужок не співпадає! ")
slovo = slovnuk.split()
if slovo:
    naidovshe_slovo = max(slovo, key=len)
    print("Найдовше слово: ",naidovshe_slovo)
else:
    print("У радку не має слів")
