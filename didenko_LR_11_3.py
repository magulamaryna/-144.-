with open("Learn_python.txt", "r", encoding="utf-8") as f:
    lines = [line.strip() for line in f]
print("Початковий текст:")
for line in lines:
    print(line)
sorted_lines = sorted(lines, key=len, reverse=True)
print("\nВідсортовано за довжиною:")
for line in sorted_lines:
    print(line)