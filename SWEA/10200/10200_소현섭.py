T = int(input())
for test_case in range(1, T + 1):
    n, a, b = map(int, input().split())
    print(f'#{test_case} {min(a, b)} {a+b-n}') if a+b-n >= 0 else print(f'#{test_case} {min(a, b)} 0')