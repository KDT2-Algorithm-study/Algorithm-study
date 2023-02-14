a,b = map(int,input().split())
n = []
for i in range(1,a+b):
    if (a%i,b%i) == (0,0):
        n.append(i)       
print(max(n))
print(a*b//max(n))