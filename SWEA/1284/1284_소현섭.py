T = int(input())
for test_case in range(1, T + 1):
    p, q, r, s, w = map(int, input().split())
    a = p*w
    if r >= w:
        b = q
    else:
        b = q + (w-r)*s
    if a < b:
        print(f'#{test_case} {a}')
    else:
        print(f'#{test_case} {b}')