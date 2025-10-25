#Завдання 1 а):
text = "Мама варить борщ. Бачу красивий вид за вікном. Чому ти плачеш?"
sentences = text.split(". ")
for i, sentence in enumerate(sentences, 1):
    words = sentence.split()
    print(f"Речення {1}: {len(words)} cлів")
#Завдання б):
longest_sentence = sentences[0]
for sentence in sentences:
    if len(sentence) > len(longest_sentence):
        longest_sentence = sentence
print("Найдовше речення: ")
print(longest_sentence)
#Завдання в):
vowels = "аоеиіу"
def remove_words(sentence):
    words = sentence.split()
    new_words = []
    for word in words:
        if len(word) < 2 or word[-2] not in vowels:
            new_words.append(word)
        return "".join(new_words)
print("Текст після видалення голосних із слів: ")
for sentence in sentences:
    print(remove_words(sentence))
#Завдання 2:
cars = [
    (20000, "легковий"),
    (35000, "вантажний"),
    (28000, "легковий"),
    (35000, "вантажний"),
    (25000, "легковий"),
    (35000, "вантажний"),
     (30000, "легковий"),
    (35000, "вантажний"),
    (30000, "легковий"),
    (40000, "вантажний")
]
total = 0
count = 0
for price, type_car in cars:
    if type_car == 'легковий':
        total += price
        count += 1
if count > 0:
    average_price = total/count
    print("Середня вартість легкових автомобілів:", average_price)
else:
    print("Легкові автомоболі наразі відсутні!")
