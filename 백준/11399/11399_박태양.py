a = int(input())
l = list(map(int,input().split()))
l = sorted(l)
total = 0
x = 0
for i in l:
    x +=i
    total += x
print(total)