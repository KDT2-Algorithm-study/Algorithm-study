import sys

n, m = map(int, sys.stdin.readline().split())
board = list()
wrong1 = [[0 for i in range(m - 7)] for i in range(n - 7)]
wrong2 = [[0 for i in range(m - 7)] for i in range(n - 7)]

for i in range(n):
    board.append(sys.stdin.readline().strip())

for i in range(n - 7):
    for j in range(m - 7):
        for k in range(j, j + 8):
            for l in range(i, i + 8):
                if (k + l) % 2:
                    if board[l][k] != 'B':
                        wrong1[i][j] += 1
                    if board[l][k] != 'W':
                        wrong2[i][j] += 1
                else:
                    if board[l][k] != 'B':
                        wrong2[i][j] += 1
                    if board[l][k] != 'W':
                        wrong1[i][j] += 1

print(min(min(map(min, wrong1)), min(map(min, wrong2))))
