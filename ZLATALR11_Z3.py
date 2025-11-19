fin = open("learning_python.txt", "r", encoding="utf-8")
lines = []
for line in fin:
    lines.append(line.strip())
fin.close()
lines.sort(key=len, reverse=True)
for l in lines:
    print(l)