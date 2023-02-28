T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    print(f'#{test_case}')
    for m in [50000, 10000, 5000, 1000, 500, 100, 50, 10]:
        print(n//m, end=' ')
        n %= m
    print()