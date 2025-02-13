s=input("Enter A String  : ")

al=0
nm=0
up=0
lw=0
sp=0
sl=0

for i in s:
    if i.isalpha():
        al=al+1
    elif i.isnumeric():
        nm=nm+1
    elif i.isspace():
        sp=sp+1
    else:
        sl=sl+1
    
    if i.isupper():
        up=up+1
    elif i.islower():
        lw=lw+1

    
    
    
print("Total Alphabets : ",al)
print("Total Numerical : ",nm)
print("Total Upper Case : ",up)
print("Total Lower Case : ",lw)
print("Total Space : ",sp)
print("Total Special Character : ",sl)
