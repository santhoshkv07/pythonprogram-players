import sys,string, math,itertools
N,g = raw_input().split()
g = int(g)
for i in range(0,g+1) :
    h = str(i)
    if h not in N :
        print('no')
        sys.exit()
print('yes')