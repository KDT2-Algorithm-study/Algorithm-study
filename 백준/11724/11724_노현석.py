import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

def dfs(N):
    visited[N] = True
    for i in range(1, n+1):
        if not visited[i] and graph[N][i]:
            dfs(i)

n, m = map(int, input().split())
graph = [[False] * (n+1) for _ in range(n+1)]
visited = [False] * (n+1)
res = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = True

for i in range(1, n+1):
    if not visited[i]:
        res += 1
        dfs(i)

print(res)