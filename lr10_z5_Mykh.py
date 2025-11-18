def func(*args, n):
    print(args)
    res = []
    for i in range(n+1):
        for j in range(len(args)):
            print(i, args[j], i % args[j])
            if i % args[j] == 0:
                res.append(i)
    return set(res)

question = int(input("Скільки чисел хочеш ввести?\n"))
count = []
for _ in range(question):
    num = int(input(f"Введи {_+1} число: "))
    count.append(num)

question_2 = int(input("Введи число: "))

print(func(*count, n=question_2))