fin = open("learning_python.txt", "r", encoding="utf-8")
fall = open("true.txt", "w", encoding="utf-8")
ffalse = open("false.txt", "w", encoding="utf-8")

for line in fin:
    if "Python" in line:
        newline = line.replace("Python", "C")
    else:
        newline = line

    print(newline.strip())

    ans = input("1 - істинно, 0 - хибно: ")

    if ans == "1":
        fall.write(newline)
    else:
        ffalse.write(newline)

fin.close()
fall.close()
ffalse.close()