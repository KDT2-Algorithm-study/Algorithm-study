case = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

t = int(input())

for i in range(t):
    n = int(input())
    # 돈의 종류에 따른 수량을 구하기 위해 딕셔너리를 하나 만든다
    result = dict.fromkeys(case, 0)

    # 큰 금액부터 수량을 구한다
    for m in case:
        if n >= m:
            result[m] = n // m
            n -= result[m] * m
    
    # 출력
    print(f'#{i + 1}')
    print(*result.values())
