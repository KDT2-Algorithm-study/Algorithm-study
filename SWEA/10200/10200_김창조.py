# 10200. 구독자 전쟁

test_case = int(input())

for tc in range(1, test_case+1):
    n, a, b = map(int, input().split())
    max_common, min_common = min(a, b), 0 if n > a + b else a + b - n
    print(f'#{tc} {max_common} {min_common}')