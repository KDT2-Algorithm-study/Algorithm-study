# 11047. 동전 0

n, k = map(int, input().split())
coin_lst = [int(input()) for _ in range(n)]
cnt = 0
for coin in coin_lst[::-1]:
    if k >= coin:
        cnt += k // coin
        k %= coin

print(cnt)