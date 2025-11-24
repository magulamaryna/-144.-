#Завдання 1
file = open("input.txt", "w", encoding="utf-8")
file.write("Ноутбук 2 15000 2023-09-12\nТелефон 6 10000 2023-11-23\nМиша 3 500 2023-08-15")
file.close()
file = open("input.txt", "r", encoding="utf-8")
lines = file.readlines()
print("Товари, що зберігаються більше місяця вартість > 1000 грн:\n")
for row in lines:
    data = row.split()
    name = data[0]
    qty = int(data[1])
    price = int(data[2])
    date = data[3]
    cost = qty * price
    if cost > 1000:
        print(name, "-", cost, "грн")

#Завдання 2
file = open("input.txt", "r", encoding="utf-8")
text = file.read()
file.close()
words = text.replace("\n", "").split()
counts = {}
for w in words:
    lw = w.lower()
    if lw in counts:
        counts[lw] += 1
    else:
        counts[lw] = 1
rezult = ""
for w in words:
    if counts[w.lower()] == 1:
        rezult += w + " "
file = open("output.txt", "w", encoding="utf-8")
file.write(rezult)
file.close()
print("\nТекст без повторюваних слів")