l=[]

for i in range(2000,3201):
    if i%5==0 and i%7!=0:
        l.append(i)
print(l)
