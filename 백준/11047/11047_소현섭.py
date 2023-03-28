n, k = map(int, input().split())
coin = sorted([int(input()) for _ in range(n)], reverse=True)
answer = 0
for i in range(0, n+1):
    if coin[i] <= k:
        answer += k // coin[i]
        k %= coin[i]
        if k == 0:
            break
print(answer)