n=int(input("enter the number:"))
l=int(input("enter the lower:"))
r=int(input("enter the higher:"))
a=list()
for i in range (0,n):
    a=int(input("number:"))
for i in range(0,n):
    if(a==l):
        print(l)
        break
    elif(a>=l):
        print(l)
        break
