T = int(input())
for test_case in range(1, T + 1):
    print(f'#{test_case} {sum([x if x%2 == 1 else -x for x in range(1, int(input())+1)])}')