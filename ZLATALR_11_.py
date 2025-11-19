file = open("students.txt", "r", encoding="utf-8")
lines = file.readlines()
file.close()
for line in lines:
    line = line.strip()
    if line == "":
        continue
    parts = line.split()
    pib = " ".join(parts[0:3])
    city = parts[3]
    score = int(parts[4])
    if city == "Київ" and score > 180:
        print("ПІБ:", pib, ", Місто:", city, ", Бал:", score)