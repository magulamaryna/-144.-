with open("numbers.txt", "r", encoding="utf-8") as f:
    numbers = [int(line.strip()) for line in f]

total = sum(numbers)

print(F"Сума чисел: {total}")
with open("sum_numbers.txt", "w", encoding="utf-8") as f:
    f.write(str(total))
