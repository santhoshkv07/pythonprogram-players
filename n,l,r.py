n,l,r=map(int,(input()).split())
a=list(map(int,(input()).split()))
b=[]
for i in range(l-1,r):
    b.append(a[i])
print(min(b))
