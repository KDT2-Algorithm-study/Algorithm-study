T = int(input())
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
for test_case in range(1, T + 1):
    d = 0
    n = int(input())
    k = 1
    li = [[0]*n for _ in range(n)]
    x, y = 0, 0
    li[x][y] = k
    while k < n**2:
        k += 1
        if 0 <= x+dx[d] <= n-1 and 0 <= y+dy[d] <= n-1 and li[x+dx[d]][y+dy[d]] == 0:
            li[x+dx[d]][y+dy[d]] = k
            x, y = x+dx[d], y+dy[d]
        else:
            d = (d + 1) % 4
            li[x+dx[d]][y+dy[d]] = k
            x, y = x+dx[d], y+dy[d]
    print(f'#{test_case}')
    for x in li:
        print(*x)