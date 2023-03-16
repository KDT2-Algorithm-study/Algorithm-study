# 1945. 간단한 소인수분해

test_case = int(input())

for tc in range(1, test_case + 1):
    n = int(input())
    lst = []
    for num in [2, 3, 5, 7, 11]:
        cnt = 0
        while not n % num:
            cnt += 1
            n /= num
        lst.append(cnt)
    
    print(f'#{tc}', *lst)