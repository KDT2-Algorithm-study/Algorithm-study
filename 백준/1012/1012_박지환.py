import sys

T = int(sys.stdin.readline())

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

for _ in range(T):
    m, n, k = map(int, sys.stdin.readline().split())
    field = [[0]*m for _ in range(n)]
    cnt = 0

    for l in range(k):
        x, y = map(int, sys.stdin.readline().split())
        field[y][x] = 1

    for i in range(n):
        for j in range(m):
            if field[i][j] == 1:
                cnt += 1
                stack = []
                stack.append(j)
                stack.append(i)

                while stack:
                    stack_i = stack.pop()
                    stack_j = stack.pop()

                    for p in range(4):
                        if 0 <= stack_i + dx[p] < n and 0 <= stack_j + dy[p] < m:
                            if field[stack_i + dx[p]][stack_j + dy[p]] == 1:
                                field[stack_i + dx[p]][stack_j + dy[p]] = 2
                                stack.append(stack_j + dy[p])
                                stack.append(stack_i + dx[p])
                