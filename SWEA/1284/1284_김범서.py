t = int(input())

for i in range(t):
    p, q, r, s, w = map(int, input().split())
    # A사 요금
    a = p * w

    # B사 요금
    if w <= r:
        b = q
    else:
        b = q + (w - r) * s

    # 더 작은 값 출력
    if a < b:
        print(f'#{i + 1} {a}')
    else:
        print(f'#{i + 1} {b}')
