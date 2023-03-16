T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    num = [2, 3, 5, 7, 11]
    index = 0
    answer = [0, 0, 0, 0, 0]
    while num[index] <= n:
        if n % num[index] == 0:
            n /= num[index]
            answer[index] += 1
        else:
            index += 1
    print(f'#{test_case}', *answer)