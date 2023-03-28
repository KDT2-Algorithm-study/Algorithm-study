n, k = map(int, input().split())
coins = []
for _ in range(n):
    num = int(input())
    coins.append(num)

cnt = 0

for coin in coins[::-1]:
    if coin <= k:
        cnt += k // coin
        k %= coin
print(cnt)