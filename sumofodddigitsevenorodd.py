n=int(input("enter the number:"))
r=0
while(n):
    s=n%10
    r=(r*10)+s
    n=n//10
print(r)
t=0
r=r//10
while(r):
    s=r%10
    t=t+s
    r=r//100
if(t%2==0):
    print("E")
else:
    print("O")

