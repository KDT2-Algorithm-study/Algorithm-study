def recursion(n, m):
    if m == 0 :
        return 1
    else:
        return n * recursion(n, m-1)

for test_case in range(1, 11) :
    T = int(input())
    n, m = map(int, input().split())
    print(f'#{test_case} {recursion(n, m)}')