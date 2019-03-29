n=int(input())
m=(list(map(int,input().split())))
a=m[0:len(ni)//2]
b=m[len(ni)//2:]
print(sorted(a)+sorted(b,reverse=True))