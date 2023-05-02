from collections import deque
import sys
input = sys.stdin.readline

dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

m, n =  map(int, input().split())
box = [[0 for i in range(m)] for j in range(n)]
points = list()
que = deque()
result = 0

for i in range(n):
	box[i] = list(map(int, input().split())
	for j in range(m):
		if box[i][j] == 1:
			que.append([i, j])

while que:
	r, c = que.popleft()
	for i in range(4):
		nr, nc = r + dr[i], c + dc[i]
		if (0 <= nr < n) and (0 <= nc < m) and not box[nr][nc]:
			box[nr][nc] = box[r][c] + 1
			que.append([nr, nc])

for i in range(n):
	for j in range(m):
		if not box[i][j]:
			print(-1)
			exit()
		if result < box[i][j]:
			result = box[i][j]

print(result - 1)
