fin = open("numbers.txt", "r", encoding="utf-8")
suma = 0
for line in fin:
    suma += int(line)
print("Сума чисел", suma)

fout = open("sum_numbers.txt", "w", encoding="utf-8")
fout.write(str(suma))
fout.close()