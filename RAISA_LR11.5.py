filename = "guest_book.txt"
while True:
    name = input("введіть ваше ім_я:")
    if not name:
        break
    welcome = f"Ласкаво просимо, {name}!"
    print(welcome)
    with open(filename, 'a', encoding="utf-8") as f:
        f.write(welcome + "\n")
print(f"\nВітання збережено, '{filename}'")