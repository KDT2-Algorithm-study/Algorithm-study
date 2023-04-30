import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
change = 0

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

tmp = [[0]*m for _ in range(n)]

q = deque()
for y in range(n):
    for x in range(m):
        if graph[y][x] == 1:
            q.append((y, x))

while q:
    y, x = q.popleft()
    for dir in range(4):
        if 0 <= y + dy[dir] < n and 0 <= x + dx[dir] < m:
            if graph[y + dy[dir]][x + dx[dir]] == 0:
                graph[y + dy[dir]][x + dx[dir]] = graph[y][x] + 1 # 1일씩 추가
                change += 1
                q.append((y + dy[dir], x + dx[dir]))

unripe , max_day = 0 # 안익은 토마토, 상자에서 가장 많이 걸린 날짜
for i in range(n):
    for j in range(m):
        if graph[i][j] > max_day:
            max_day = graph[i][j]
        elif graph[i][j] == 0: # 토마토가 하나라도 익지 않았을 경우
            unripe += 1
            break

if unripe == 0:
    print(max_day - 1) # 시작일이 1일이었으므로 1을 뺀다.
else:
    print(-1) 