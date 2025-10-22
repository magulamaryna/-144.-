def operator(code):
    vodafone = ["050", "066", "095", "099", "075"]
    kyivstar = ["039", "067", "068", "096", "097", "098", "077"]
    lifecell = ["063", "093", "073"]

    if code in vodafone:
        return "У вас оператор Водафон"
    elif code in kyivstar:
        return "У вас оператор Київстар"
    elif code in lifecell:
        return "У вас оператор Лайвсел"
    else:
        return "Такого коду нема"

num = input("Введи код оператора:\n")

print(operator(num))