vowels = "аоуеиіїєюя"
fin = open("input.txt", "r", encoding="utf-8")
fout = open("output.txt", "w", encoding="utf-8")
text = fin.read()
for ch in ",.!?;:-":
    text = text.replace(ch, " ")
words = text.split()
new_words = []
for word in words:
    uniq = set()
    for c in word.lower():
        if c in vowels:
            uniq.add(c)
    if len(uniq) <= 2:
        new_words.append(word)
fout.write(" ".join(new_words))
fin.close()
fout.close()
print("Готово!")