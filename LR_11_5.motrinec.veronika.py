n = int(input("кількість імен"))
with open("guest_book.txt", "w", encoding="utf-8") as file:
    for i in range(n):
        name = input("ведіть ім'я")
        greeting = f"вітаю!!{name}"
        print(greeting)
        file.write(greeting)
