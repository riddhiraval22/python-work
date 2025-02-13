'''
n=int(input("Enter N : "))
sum=0
for i in range(1,n+1):
    sum=sum+i
print("Sum : ",sum)

*
**
***
****
*****
    *
   **
  ***
 ****
*****
'''

n=int(input("Enter N : "))

for i in range(n,0,-1):
    print(" "*(n-i)," *"*i)




