print("Введіть цілі:")
input_string = input()
input_numbers = input_string.split()
out_lines = []
for i in input_numbers:
    try:
        number = int(i)
        if number % 2 == 0:
            rezult = "парне"
        else:
            rezult = "непарне"
        out_line = f"Число {number}: {rezult}."
        out_lines.append(out_line)
    except ValueError:
        out_lines.append(f"'i' проігноровано.")
try:
    with open("_rezults.txt", "w", encoding="utf-8") as f:
        f.write('\n'.join(out_lines) + '\n')
    print("\n Файл створено")
except IOError:
    print("Помилка при записі у файл")