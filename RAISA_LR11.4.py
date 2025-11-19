source_file = "learning_python.txt"
updated_file = "learning_c.txt"
false_file = "false_statements.txt"
with open(source_file, 'r', encoding="utf-8") as f:
    lines = f.readlines()
updated_lines = []
false_lines = []
for line in lines:
    updated_line = line.replace("Python", "C")
    print("\n" + updated_line.strip())
    answer = input("Павильно для С? (y/n): ").strip().lower()
    if answer == 'y':
        updated_lines.append(updated_line)
    else:
        false_lines.append(updated_line)
with open(updated_file, 'w', encoding="utf-8") as f:
    for i in updated_lines:
        f.write(i)
with open(false_file, 'w', encoding="utf-8") as f:
    for i in false_lines:
        f.write(i)
print(f"\n Фрази збережено у {updated_file}")
print(f"Хибні збережено у {false_file}")
