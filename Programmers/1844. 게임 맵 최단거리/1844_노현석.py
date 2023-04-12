from collections import deque

def bfs(dx, dy, maps, n, m):
    q = deque()
    q.append((0,0))

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx > m or ny > n:
                continue
            if maps[nx][ny] == 0:
                continue
            if maps[nx][ny] == 1:
                maps[nx][ny] += maps[x][y]
                q.append((nx, ny))
    return maps[m][n]

def solution(maps):
    n = len(maps[0]) - 1
    m = len(maps) - 1
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    answer = bfs(dx, dy, maps, n, m)
    if answer == 1:
        answer = -1
    return answer