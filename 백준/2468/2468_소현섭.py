import sys
sys.setrecursionlimit(100000)

def dfs(x, y, h):
    for m in range(4):
        nx = x + dx[m]
        ny = y + dy[m]
        if (0 <= nx < n) and (0 <= ny < n) and not sink_table[nx][ny] and li[nx][ny] > h:
            sink_table[nx][ny] = 1
            dfs(nx, ny, h)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
n = int(sys.stdin.readline())
li = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
ans = 0
for k in range(max(map(max, li))):
    sink_table = [[0]*n for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(n):
            if li[i][j] > k and not sink_table[i][j]:
                count += 1
                sink_table[i][j] = 1
                dfs(i, j, k)
    ans = max(ans, count)

print(ans)