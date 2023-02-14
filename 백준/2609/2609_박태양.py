import math
a,b = map(int,input().split())
g = math.gcd(a,b)
print(g)
print(a*b//g)