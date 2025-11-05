def func(sentence):
    vowels = "аяоуюеєиіїАЯОУЮЕЄИІЇ"
    words = sentence.split()
    splited_w = []
    palindromy = []
    same_words = 0

    for word in words:
        word = list(word)
        splited_w.append(word)

    for w in splited_w:
        vowel = 0
        other = 0
        for letter in "".join(w).lower():
            if letter.isalpha() and letter in vowels:
                vowel += 1
            if letter.isalpha() and letter not in vowels:
                other += 1
        if vowel == other:
            same_words += 1
    
    for w in splited_w:
        if "".join(w).lower() == "".join(w)[::-1].lower():
            palindromy.append("".join(w))

    return f"Однакових слів: {same_words}\nНайдовше слово: {max(words, key=len)}\nслова паліндроми: {", ".join(palindromy)}"

sentence = input("Введи речення або набір слів:\n")

print(func(sentence))