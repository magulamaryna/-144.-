text = open("pytho_ststa.txt","r",encoding="utf-8").read().lower()
letters = {}
words = {}
for i in text:
    if i.isalpha(): letters[i] = letters.get(i, 0) + 1
for j in text.split():
    words[j] = words.get(j, 0) + 1
f = open("result.txt","w",encoding="utf-8")
f.write("letters:\n")
for w in letters: f.write(f"{w}{letters[w]} \n")
f.write("\nwords(top 10):\n")
for j,v in sorted(words.items(), key = lambda x:x[1], reverse = True)[:10]:
    f.write(f"{j} {v} \n")
f.close()
print("done, results saved to result.txt")
