import datetime
f = open("book.txt", "a", encoding="utf-8")
while True:
    name = input("Введіть ваше ім'я (або 'stop' для виходу): ")
    if name == "stop":
        break
    time_now = datetime.now()
    message = "Привіт, " + name + "! Вітаємо вас у нашій книзі гостей! (" + str(time_now) + ")"
    print(message)
    f.write(message + "\n")
f.close()