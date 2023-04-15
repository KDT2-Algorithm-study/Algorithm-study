from collections import deque

def bfs(x, y):
    q.append((x, y))
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if (0 <= nx < N and 0 <= ny < N) and (graph[nx][ny] == graph[x][y]) and not (visited[nx][ny]):
                visited[nx][ny] = 1
                q.append((nx,ny))


N = int(input())
graph = [list(input()) for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
q = deque()
answer1, answer2 = 0, 0
visited = [[0] * N for _ in range(N)]

for a in range(N):
    for b in range(N):
        if not visited[a][b]:
            bfs(a, b)
            answer1 += 1

for c in range(N):
    for d in range(N):
        if graph[c][d] == 'R':
            graph[c][d] = 'G'

visited = [[0] * N for _ in range(N)]

for e in range(N):
    for f in range(N):
        if not visited[e][f]:
            bfs(e, f)
            answer2 += 1

print(answer1, answer2)