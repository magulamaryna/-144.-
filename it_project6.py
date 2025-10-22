for i in range(10, 101, 3):
    print(i)

print("\n")

text = input("text:\n")

for i in range(len(text)):
    print(f"char {i+1}: {text[i]}")
    if text[i] == "a":
        print("I found a")

print("\n")

i = 0
while i < len(text):
    i += 1
    print(f"now i is {i}")
    if i > 20:
        print("I is more than 20")

print("\n")

for i in range(2**100):
    if i % 2 == 0:
        continue
    print(i)
    if i == 333:
        break