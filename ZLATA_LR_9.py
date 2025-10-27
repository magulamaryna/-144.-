text = input("Введіть текст")

small_letters = 0
for letters in text:
    if letters >= "a" and letters <= "Z":
      small_letters +=1
print("Кількість маленьких літер", small_letters)

words = text.split()
max_len = 0
for w in words:
    if len(w) > max_len:
        max_len = len(w)

print("Слова з найбільшою кількістю літер")
for w in words:
    if len(w) == max_len:
        print(w)
new_words = []
for w in words:
    if not (w[0] >= "A" and w[0] <= "Z"):
        new_words.append(w)
print("Текст без слів що починається з великої літери")
print("".join(new_words))

