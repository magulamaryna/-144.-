with open("learning_python.txt", "r", encoding="utf-8") as f:
    lines = [line.strip() for line in f if line.strip()]
for line in lines:
    print(line)
lines.sort(key=len, reverse=True)
print("\nВідсортовані рядки за довжиною:")
for line in lines:
    print(f"[{len(line)}]: {line}")