from collections import deque

dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]


# BFS
def bfs(row, col):
    que = deque([(row, col)])
    while que:
        r, c = que.popleft()
        for l in range(4):
            nr, nc = r + dr[l], c + dc[l]
            if (0 <= nr < n) and (0 <= nc < n):
                if not chk[nr][nc] and area[nr][nc] > i:
                    chk[nr][nc] = True
                    que.append((nr, nc))


n = int(input())
area = [[0 for i in range(n)] for j in range(n)]
result = list()
min_height = 1001
max_height = 0

# 데이터를 입력받고 최대 높이와 최소 높이를 구한다
for i in range(n):
    area[i] = list(map(int, input().split()))
    for j in range(n):
        if area[i][j] < min_height: min_height = area[i][j]
        if area[i][j] > max_height: max_height = area[i][j]

# 최소 높이보다 1 작은 높이부터 최대 높이까지의 범위를 돌며
# 각 높이별 영역의 수를 센다
for i in range(min_height - 1, max_height + 1):
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
