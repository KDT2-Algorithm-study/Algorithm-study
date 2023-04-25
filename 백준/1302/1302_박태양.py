import sys
input = sys.stdin.readline
d = {}
l = []
for _ in range(int(input())):
    a = input()
    d[a] = d.get(a,0) + 1

l= list(d.items())
l = sorted(l,key =lambda x : (-x[1],x[0]))
print(l[0][0])