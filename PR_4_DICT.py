student = {
    "st1":"Заводяк Віталіна",
    "st2":"Депутатенко Максим",
    "st3":"Іванцюк Михайло"
}
print(student["st2"])
print(student)
student["st4"]="Магула Іванна"
print(student)


found = {
    7:"Катреняк",
    26:"Черевко",
    15:"Попина",
    19:"Сойма",
    6:"Кручінін"
}
for i,j in sorted(found.items()):
    print(i, "має значення", j)

slovnuk_2 = dict(
    ivan="Програміст",
    valentina="Лікар",
    sofia="Перукар",
    darija="Історик",
    lidija="Біолог"
)

if "darija" in slovnuk_2:
    print("Є такий ключ - darija")
else:
    print("Нема такого ключа - darija")

del(slovnuk_2["lidija"])
