from collections import deque

def bfs():
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            a = x+dx[i]
            b = y+dy[i]
            if 0 <= a < n and 0 <= b < m and graph[a][b] == 0:
                queue.append([a,b])
                graph[a][b] = graph[x][y]+1

m,n = map(int,input().split())
graph = []
queue = deque([])
dx = [-1,1,0,0]
dy = [0,0,-1,1]

for i in range(n):
    graph.append(list(map(int,input().split())))
    for j in range(m):
        if graph[i][j] == 1:
            queue.append([i, j])

bfs()
answer = 0
for i in graph:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    answer = max(answer, max(i))
print(answer-1)
