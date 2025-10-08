book = "Магула Марина Віталіївна"
booklist = list(book)
print(book)
print(booklist)
print(booklist[0:3])
print(booklist[4:11])
zriz_str = "".join(booklist[4:11])
print(zriz_str)
#join - перетворює список у рядок
#list - створює контейнерну змінну список
#copy - копіювання одного списку в інший
#[0:3] - зріз в списку
#insert - додає елемент в список з лівої сторони списку
#append - додає елементи в список з правої сторони списку
#extend - об'єднує два списку
#remove - видаляє значення зі списку
#pop - видаляє індекс у списку
#подача індексу з "-", означає обробку елементів з кінця списку
l_vuvid = []
l_vuvid = booklist[24:13:-1]
print(l_vuvid)
l_vuvid = "".join(booklist[24:13:-1])
print(l_vuvid)
l_vuvid_1 = "".join(booklist[12:6:-1])
print(l_vuvid_1)
l_vuvid_2 = "".join(booklist[14]+booklist[15]+booklist[16]+booklist[1]+booklist[0]+booklist[15]+booklist[22])
print(l_vuvid_2)
list_2 = [2,7,[3,5,[[5,0,1,56],6,0.7],9,"d","gfdt"],8,9,2]
list_2[2][5]=list(list_2[2][5])
print(list_2)
list_2[2][5][1]="A"
print(list_2)
list_2[2][2][2]="A"
print(list_2)
for i in range(len(booklist[0:13])):
    booklist[i]="A"
print(booklist)