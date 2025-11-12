def inside_circle(x,y,a,b, R):
    distance_squared = (x - a)**2 + (y-b)**2
    return distance_squared < R**2
print("Введіть параметри кола")
a = float(input("Координати центра a ="))
b = float(input("Координати центра b ="))
R = float(input("Радіус R ="))
print("\n Введіть координати точок")
p1 = float(input("p1 = "))
p2 = float(input("p2 = "))
f1 = float(input("f1 = "))
f2 = float(input("f2 = "))
l1 = float(input("l1 = "))
l2 = float(input("l2 = "))
count = 0
if inside_circle (p1,p2,a,b,R):
    count +=1
if inside_circle(f1,f2,a,b,R):
     count+=1
if inside_circle(l1,l2,a,b,R):
     count+=1
print("\n Кількість точок усередині кола", count)