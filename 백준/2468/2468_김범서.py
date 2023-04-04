from collections import deque

dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

def bfs(row, col):
    que = deque([(row, col)])

    while que:
        r, c = que.pop()

        for l in range(4):
            nr = r + dr[l]
            nc = c + dc[l]
            if (0 <= nr < n) and (0 <= nc < n):
                if not chk[nr][nc] and area[nr][nc] > i:
                    chk[nr][nc] = True
                    que.appendleft((nr, nc))

n = int(input())
area = [[0 for i in range(n)] for j in range(n)]
result = list()
minH = 1001
maxH = 0

for i in range(n):
    area[i] = list(map(int, input().split()))
    for j in range(n):
        if area[i][j] < minH:
            minH = area[i][j]
        if area[i][j] > maxH:
            maxH = area[i][j]

for i in range(minH - 1, maxH + 1):
    chk = [[False for j in range(n)] for k in range(n)]
    cnt = 0
    for j in range(n):
        for k in range(n):
            if area[j][k] > i and not chk[j][k]:
                chk[j][k] = True
                cnt += 1
                bfs(j, k)
    result.append(cnt)

print(max(result))
