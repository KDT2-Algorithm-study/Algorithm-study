T = int(input())

for tc in range(1, T+1):
    n, a, b = map(int, input().split())
    if a+b > n:
        min_ = a + b - n
    else:
        min_ = 0

    print(f'#{tc} {min(a, b)} {min_}')