
with open("input.txt", "r", encoding="utf-8") as file:
    text = file.read()
with open("diction.txt", "r", encoding="utf-8") as file:
    vudaleni_words = file.read().split()
words = text.split()
result = []
for word in words:
    clean = word.strip(".,!:;").lower()
    if clean not in vudaleni_words:
        result.append(word)
output = " ".join(result)
with open("output.txt", "w", encoding="utf-8") as file:
    file.write(output)

