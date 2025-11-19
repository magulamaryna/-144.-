i = 0
with open("numbers.txt","r") as f:
    for word in f:
        i += int(word.strip())
with open("sum.numbers.txt","w") as f:
    f.write(str(i))
print("сума чисел у файлі numbers.txt",i)
