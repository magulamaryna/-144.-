def adcler(*nums):
    sum=0
    for n in nums:
        sum+=n
    print("sum",sum)
adcler(3,5)
adcler(4,5,6,7)
adcler(1,2,3,4)
a = [1,2,3]
b=[*a,4,5,6]
print(b)
def printPetnames(owner,**pets):
    print(f"owner Name:{owner}")
    for pet,name in pets.items():
        print (f"{pet}:{name}")
printPetnames("ivan",dog="rex",fish=["burney","homer","moe"],tuerle="shelldon")
