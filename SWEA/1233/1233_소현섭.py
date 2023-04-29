T = 10
for test_case in range(1, T + 1):
    try:
        n = int(input())
        li = [input().split()[1:] for _ in range(n)]
        answer = 0
        for x, y in zip(li[::-1], range(n-1, -1, -1)):
            if len(x) != 1:
                if x[0] == '+':
                    li[y] = [int(li[int(x[1])-1][0]) + int(li[int(x[2])-1][0])]
                elif x[0] == '-':
                    li[y] = [int(li[int(x[1])-1][0]) - int(li[int(x[2])-1][0])]
                elif x[0] == '*':
                    li[y] = [int(li[int(x[1])-1][0]) * int(li[int(x[2])-1][0])]
                elif x[0] == '/':
                    if int(li[int(x[2])-1][0]) == 0:
                        li[y] = [int(li[int(x[1])-1][0])]
                    else:
                        li[y] = [int(li[int(x[1])-1][0]) // int(li[int(x[2])-1][0])]
                else:
                    a = 1/0
        print(f'#{test_case} 1')
    except:
        print(f'#{test_case} 0')