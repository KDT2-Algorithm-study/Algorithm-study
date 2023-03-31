T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    price = list(map(int,input().split()))
    result, max_price = 0, 0
    for i in range(n-1,-1,-1):
        if price[i] > max_price:
            max_price = price[i]
        else:
            result += max_price - price[i]
    print(f'#{test_case} {result}')