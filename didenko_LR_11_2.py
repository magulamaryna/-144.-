nums = input("Введіть довільну кількість чисел через пробіл:").split()
nums = [int(x) for x in nums]
with open("parity.txt","w", encoding="utf-8") as f:
    for n in nums:
        if n % 2 == 0:
            f.write(F"{n}- парне\n")
        else:
            f.write(F"{n}- непарне\n")
print("\nВміст файлу:\n")
with open("parity.txt","r", encoding="utf-8") as f:
    print(f.read())