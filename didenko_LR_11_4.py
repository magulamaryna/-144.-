import os
os.makedirs("C_language", exist_ok=True)
with open("Learn_python.txt", "r", encoding="utf-8") as f:
    lines = [line.strip() for line in f]
correct = []
incorrect = []
for line in lines:
    new_line = line.replace("Python", "C")
    print(new_line)
    ans = input("Чи є твердження правильним? (так/ні): ").strip().lower()
    if ans == "так":
        correct.append(line)
    else:
        incorrect.append(line)
with open("C_language.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(correct))
with open("C_language.txt", "r", encoding="utf-8") as f:
    f.write("\n".join(incorrect))