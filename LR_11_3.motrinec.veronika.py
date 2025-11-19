print("файл")
with open("learning_python.txt", "r", encoding="utf-8") as file:
    lines = []
    for line in file:
        line = line.strip()
        print(line)
        lines.append(line)
sorted_line = sorted(lines, key=len, reverse=True)
for line in sorted_line:
    print(line)