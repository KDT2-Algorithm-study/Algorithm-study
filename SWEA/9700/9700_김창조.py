# 9700. USB 꽂기의 미스터리

test_case = int(input())

for tc in range(1, test_case+1):
    p, q = map(float, input().split())
    s1 = (1 - p) * q
    s2 = p * (1 - q) * q
    answer = 'YES' if s1 < s2 else 'NO'
    print(f'#{tc} {answer}')