from datetime import datetime
import time
start_time = time.time()
fin = open("python_article.txt", "r", encoding="utf-8")
text = fin.read()
fin.close()
text_lower = text.lower()
letter_freq = {}
for char in text_lower:
    if char.isalpha():
        if char in letter_freq:
            letter_freq[char] += 1
        else:
            letter_freq[char] = 1
words = text_lower.split()
word_freq = {}
for word in words:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1
end_time = time.time()
elapsed_time = end_time - start_time
print("Частота літер")
for letter in sorted(letter_freq):
    print(letter, letter_freq[letter])
print("\nЧастота слів")
for word in sorted(word_freq, key=lambda x: word_freq[x], reverse=True):
    print(word, word_freq[word])
print("\nЧас початку аналізу:", datetime.now())
print("Час, затрачений на пошук:", round(elapsed_time, 2), "секунд")