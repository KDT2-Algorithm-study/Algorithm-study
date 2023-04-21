T = int(input())
for test_case in range(1, T + 1):
    p, q = map(float, input().split())
    print(f'#{test_case} YES')if (p * (1-q) * q) > ((1-p) * q) else print(f'#{test_case} NO')