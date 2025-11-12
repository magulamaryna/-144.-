def prosti_chusla(n):
    proste = []
    for num in range(2,n+1):
        is_proste = True
        for i in range(2, num):
            if num % i ==0:
                is_proste = False
                break
        if is_proste:
            proste.append(num)
    return proste
n = int(input("Введіть число n"))
print("Оберіть формат виводу")
print("1 список")
print("2 стовпчик")
print("3 кількість простих чисел")
vubir = int(input("Ваш вибір"))
result = prosti_chusla(n)
if vubir ==1:
    print("Список простих чисел", result)
elif vubir == 2:
    print("Прості числа в стовпчик")
    for i in result:
        print(i)
elif vubir == 3:
    print("Кількість простих чисел", len(result))
else:
    print("Неправильний вибір")

