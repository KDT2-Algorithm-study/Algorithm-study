N, K = map(int, input().split())
coins = []
cnt = 0
for _ in range(N):
    coins.append(int(input()))

for _ in range(N):
    coin = coins.pop()
    if K // coin > 0:
        cnt += K // coin 
        K %= coin
print(cnt)
