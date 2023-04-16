T = int(input())

for i in range(1, T+1):
    n, a, b = map(int, input().split())

    print(f'#{i} {min(a, b)} {max(0, (a+b) - n)}')