#1
text = input("ведіть текст")
#a
digits = 0
for i in text:
    if i.isdigit():
        digits += 1
print("кількість цифр",digits)
#b
vowels = "аеєиіїоуюяАЕЄИШЇОУЮЯ"
for word in text.split():
    if word[0] not in vowels:
        print(word)
#v
for word in text.split():
    if word[0].lower() != word[-1].lower():
        print(word)