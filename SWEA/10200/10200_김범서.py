t = int(input())

for i in range(t):
    n, a, b = map(int, input().split())
    big = min(n, min(a, b))
    small = max(0, a + b - n)
    print(f'#{i + 1} {big} {small}')
