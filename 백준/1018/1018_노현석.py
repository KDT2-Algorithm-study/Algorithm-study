def check(n, m):
    cnt = 0
    for x in range(n, n+8):
        for y in range(m, m+8):
            if (x+y) % 2 == 0 and board[x][y] == 'B':
                cnt += 1
            if (x+y) % 2 == 1 and board[x][y] == 'W':
                cnt += 1
    change=min(cnt, 64-cnt)
    return change

n, m = map(int, input().split())
board = [input() for i in range(n)]
res = 64
for i in range(0, n-7):
	for k in range(0, m-7):
            res = min(res, check(i, k))
print(res)