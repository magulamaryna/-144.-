import math
def kolo (x,y,a,b,R):
    return (x-a)**2 + (y-b)**2<R**2
a,b=0,0
R = 6
tochku = {
    "P": (6,9),
    "F": (-6,4),
    "L": (1,2)
}
i = 0
for v,(x,y) in tochku.items():
    if kolo(x,y,a,b,R):
        print(f"точка {v} всередині кола")
        i += 1
    else:
        print(f"точка {v} нe всередені кола")
print("точки в колі", i)