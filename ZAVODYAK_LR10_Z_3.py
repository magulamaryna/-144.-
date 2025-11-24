def in_kolo(x, y, a, b, R):
    return (x - a)**2 + (y-b)**2 < R**2

a = float(input("ведіть а "))
b = float(input("ведіть b "))
R = float(input("ведіть радіус R "))

points = []
for name in ['P', 'F', 'L']:
    x = float(input(f"ведіть {name}x "))
    y = float(input(f"ведіть {name}y "))
    points.append((x, y))

count = 0
for (x, y) in points:
    if in_kolo(x, y, a, b, R):
        count += 1
print("кількість кола у середині", count)




