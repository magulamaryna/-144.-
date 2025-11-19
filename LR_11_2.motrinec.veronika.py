n = int(input("скільки чисел"))
with open("numbers2.txt","w", encoding="utf-8") as file:
    for i in range(n):
        numbers = int(input("ведіть число"))
        if numbers % 2 == 0:
            file.write(str(numbers) + "парне число\n")
        else:
            file.write(str(numbers)+ "непарне число\n")
