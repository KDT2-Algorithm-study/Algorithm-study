def div(n, m):
    cnt = 0
    while not n % m:
        cnt += 1
        n //= m
    return cnt

t = int(input())

for i in range(t):
    n = int(input())
    a = div(n, 2)
    b = div(n, 3)
    c = div(n, 5)
    d = div(n, 7)
    e = div(n, 11)
    print(f'#{i + 1}', a, b, c, d, e)
