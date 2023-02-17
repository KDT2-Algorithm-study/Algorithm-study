a, b = map(int, input().split())

if a > b:
    min_ab = a
    max_ab = b
else:
    min_ab = b
    max_ab = a

lst = []

for n in range(1,min_ab+1):
    if a % n == 0 and b % n == 0:
        lst.append(n)
ml = max(lst)
print(ml)

(a//ml) * (b//ml)

print(ml * (a//ml) * (b//ml))