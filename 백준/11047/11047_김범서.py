n, k = map(int, input().split())
cnt =  0
coin = list()

for i in range(n):
    coin.append(int(input()))

# 액면가가 높은 동전부터 센다
for i in range(n - 1, -1, -1):
    if k >= coin[i]:
        cnt += (k // coin[i])
        k -= coin[i] * (k // coin[i])
    if k == 0:
        break

print(cnt)
