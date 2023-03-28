n, k = map(int, input().split())
coin = [int(input()) for _ in range(n)]

res = 0
for i in range(n - 1, -1, -1):
    if k >= coin[i]:
        res += k // coin[i]
        k = k % coin[i]

print(res)