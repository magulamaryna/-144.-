n = int(input("ведіть кількість співробітників"))
for i in range(n):
    name = input("ПІБ ")
    hours = float(input("ведіть кількість відпрацьованих годин "))
    rate = float(input("погодинний тариф"))
def calk_salary(name,hours, rate):
    norm = 144
    if hours <= norm:
        gross = hours * rate
    else:
        overtime = hours - norm
        gross = norm * rate + overtime * rate * 2

    net_salary = gross * 0.88
    return net_salary
salary = calk_salary(name,hours, rate)
print("заробітна плата", name)
print("після податку", salary)


