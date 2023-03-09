def exp(n, m):
    # 0의 거듭제곱은 0
    if not n: return 0
    # 어떤 수의 0제곱은 1
    if not m: return 1

    # n * n^(m - 1)
    return n * exp(n, m - 1)

for i in range(10):
    t = int(input())
    a, b = map(int, input().split())
    answer = exp(a, b)
    print(f'#{t} {answer}')


# 어제(3월 8일) 분할정복으로 거듭제곱 문제를 푸는 영상을 보고
# 백준에서 관련 문제를 풀어봤는데 복습 겸 한 번 다시 시도해보았다
'''
def exp(n, m):
    if not n: return 0
    if not m: return 1

    result = exp(n, m // 2)
    return (n * result * result) if m % 2 else (result * result)

for i in range(10):
    t = int(input())
    a, b = map(int, input().split())
    # 이 문제에서는 b가 0 이상인 정수인 경우만 다루지만
    # 만약 b가 음수라면 b의 절대값을 인수로 넘겨준 후
    # 1을 결과값으로 나누면 된다
    answer = exp(a, b)
    print(f'#{t} {answer}')
'''
