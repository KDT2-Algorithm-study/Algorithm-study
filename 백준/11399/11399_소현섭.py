n = int(input())
p = sorted(list(map(int, input().split())))
answer = 0
for x in range(n):
    answer += p[x]*(n-x)
print(answer)