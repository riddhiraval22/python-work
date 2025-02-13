t=(1,2,1.1,2.2,10,20,[100,200,300],"tops","python",True,False)

print(t)
print(t.count(1))
print(t.index(10))

for i in t:
    print(i)
print(201 in t)
print(t[6])
t[6].append(400)
print(t)
print(list(t))
