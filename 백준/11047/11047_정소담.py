n,m = map(int,input().split())
coin = [int(input()) for _ in range(n)][::-1]
cnt = 0

for i in coin:
    cnt += m // i
    m = m % i
print(cnt)