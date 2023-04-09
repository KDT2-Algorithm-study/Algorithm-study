T = int(input())
for t in range(1, T+1):
    result = 0
    N = int(input())
    num = list(map(int, input().split()))
    max_num = num[-1]
    for num in num[::-1]:
        if max_num > num:
            result +=  max_num - num
        elif max_num <= num:
            max_num = num  

    print(f"#{t} {result}")