from datetime import datetime
f = "guest_book.txt"
open(f, "a", encoding="utf-8").write(f"Створено: {datetime.now() :%Y-%m-%d %H:%M:%S}\n\n") if not open(f).readable() else None
while True:
    name = input("Ім'я (stop)").strip()
    if name.lower() == "stop": break
    line = f"{datetime.now():%Y-%m-%d %H:%M:%S} - Вітаю, {name}!\n"
    print(line.strip())
    open(f, "a", encoding="utf-8").write(line)
open(f, "a", encoding="utf-8").write(f"\nОстанні зміни: {datetime.now() :%Y-%m-%d %H:%M:%S}\n")