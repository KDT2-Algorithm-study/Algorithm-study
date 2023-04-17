import sys
sys.setrecursionlimit(1000000)

n = int(sys.stdin.readline())
matrix = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
visited = [[False] * n for _ in range(n)] # 방문 기록

dx = [1, 0, -1, 0] # 방향을 나타냄
dy = [0, -1, 0, 1]

cnt2, cnt3 = 0, 0

def dfs(x, y):
    visited[x][y] = True
    color = matrix[x][y]

    for dir in range(4):
        nx = x + dx[dir]
        ny = y + dy[dir]

        if 0 <= nx < n and 0 <= ny < n:
            if visited[nx][ny] == False:
                if matrix[nx][ny] == color:
                    dfs(nx, ny)


for i in range(n): # 적록색약이 아닌 사람
    for j in range(n):
        if visited[i][j] == False:
            dfs(i, j)
            cnt3 += 1

for i in range(n): # 적록색약으로 만들기
    for j in range(n):
        if matrix[i][j] == 'R':
            matrix[i][j] = 'G'

visited = [[False] * n for _ in range(n)] # 방문 기록 갱신

for i in range(n): # 적록색약인 사람
    for j in range(n):
        if visited[i][j] == False:
            dfs(i, j)
            cnt2 += 1

print(cnt3, cnt2)