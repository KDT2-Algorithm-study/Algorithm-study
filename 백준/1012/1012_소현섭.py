import sys
sys.setrecursionlimit(10000)

def dfs(x, y):
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < m) and (0 <= ny < n): 
            if graph[ny][nx] == 1:
                graph[ny][nx] = -1
                dfs(nx, ny)

for i in range(int(input())):
    m, n, k = map(int, input().split())
    graph = [[0]*m for _ in range(n)]
    answer = 0

    for j in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1

    for a in range(m):
        for b in range(n):
            if graph[b][a] == 1:
                dfs(a, b)
                answer += 1

    print(answer)