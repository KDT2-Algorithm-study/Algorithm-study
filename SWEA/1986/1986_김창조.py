# 1986. 지그재그 숫자

test_case = int(input())

for case in range(1, test_case+1):
    n = int(input())
    if n % 2 == 0:
        answer = n // 2 * -1
    else:
        answer = n // 2 + 1
    
    print(f'#{case} {answer}')