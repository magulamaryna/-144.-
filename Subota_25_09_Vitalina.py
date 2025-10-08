vodafon = ["095", "055", "066", "050", "099"]
kuivstar = ["096", "097", "068", "067", "098"]
lifesell = ["063", "073", "093"]
kod = input("Введіть код оператора")
if kod in vodafon:
    print("Код належить оператору Vodafon!")
elif kod in kuivstar:
    print("Код належить оператору Київстар!")
elif kod in lifesell:
    print("Код належить оператору Lifesell!")
else:
    print("Я не знаю такого оператора!")