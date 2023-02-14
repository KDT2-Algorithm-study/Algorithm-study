a, b = map(int, input().split())
gcd = 0
for x in range(min(a, b), 0, -1):
    if a % x == 0 and b % x == 0:
        gcd = x
        break
print(gcd, a*b//gcd)