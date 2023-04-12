from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    que = deque([(0, 0)])
    maps[0][0] = 2
    while que:
        r, c = que.popleft()
        for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            nr, nc = r + dr, c + dc
            if (0 <= nr < n) and (0 <= nc < m):
                if maps[nr][nc] == 1:
                    maps[nr][nc] = maps[r][c] + 1
                    que.append((nr, nc))
    return maps[n - 1][m - 1] - 1 if maps[n - 1][m - 1] != 1 else -1
