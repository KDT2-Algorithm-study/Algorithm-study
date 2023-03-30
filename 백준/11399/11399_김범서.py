n = int(input())
p = list(map(int, input().split()))
p.sort()

result = 0
for i in range(1, n + 1):
    result += sum(p[:i])
print(result)
