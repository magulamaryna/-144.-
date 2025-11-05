def zamina(a):
    for i in range(len(a)):
        if a[i] % 2!=0:
            a[i+1]=0
    return a
a = [1,3,4,5,6]
a = zamina(a)
print(a)