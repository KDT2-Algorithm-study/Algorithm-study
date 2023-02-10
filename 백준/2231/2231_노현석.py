def div_add(n):
    num = [int(i) for i in str(n)]
    return sum(num)

n = int(input())
res = 0
cnt = 0

for _ in range(n):
    if n == (cnt + div_add(cnt)):
        res = cnt
        break
    cnt += 1

print(res)