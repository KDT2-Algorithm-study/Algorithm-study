from collections import deque

direct = [(1,0), (0,1), (-1,0), (0,-1)]
n = int(input())
paint = [input() for _ in range(n)]
paint2 = []

for i in paint:
    j = i.replace('R','G')
    paint2.append(j)

def bfs(x, y, z):
    queue.append((x, y))
    visit[x][y] = 1
    while queue:
        x, y = queue.popleft()
        for d in direct:
            xd, yd = x + d[0], y + d[1]
            if 0 <= xd < n and 0 <= yd < n:
                if z[xd][yd] == z[x][y] and visit[xd][yd] == 0:
                    visit[xd][yd] = 1
                    queue.append((xd,yd))

cnt = 0
visit = [[0]*n for _ in range(n)]
queue = deque()                 
for x in range(n):
    for y in range(n):
        if visit[x][y] == 0:
            bfs(x, y, paint)
            cnt += 1


cnt2 = 0
visit = [[0]*n for _ in range(n)]
queue = deque()
for x in range(n):
    for y in range(n):
        if visit[x][y] == 0:
            bfs(x, y, paint2)
            cnt2 += 1

print(cnt, cnt2)