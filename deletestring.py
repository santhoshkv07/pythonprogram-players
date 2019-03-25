s=input("enter s")
t=input("enter t")
s1=s.split(" ")
l=[]
for i in range(len(s1)):
    l.append(len(s1[i]))
    c=max(l)
    if s1[i]==t:
        s1[i]='*';
for i in range(len(s1)):
    if s1[i]!='*':
        print(s1[i]);
