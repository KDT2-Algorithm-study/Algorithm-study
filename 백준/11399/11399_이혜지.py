n = int(input())
li = list(map(int, input().split()))

li.sort()
t = 0 
for x in range(1, n+1):
    t += sum(li[0:x])
print(t)