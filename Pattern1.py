n=int(input("Enter ASCII Code For Alphabet Pattern(65-90) : "))

for i in range(n,n+10):
    print(" "*((n+10)-i),end="")
    for j in range(n,i):
        print(chr(j),end=" ")
    print()
    
