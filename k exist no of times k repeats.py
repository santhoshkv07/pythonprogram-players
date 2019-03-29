n=int(input())
x=int(input())
s=[int(x)for x in input().split()]
c=0
for i in range (0,n):
  if s[i]==x:
    c=c+1
if c>=1:
  print('yes',c)
else:
  print('no')