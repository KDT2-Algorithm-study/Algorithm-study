import sys
N, K = map(int, sys.stdin.readline().split())
coins = [ int(sys.stdin.readline()) for _ in range(N)]
coins = reversed(coins)
cnt = 0
for c in coins:
    cnt += K // c
    K %= c
print(cnt)
