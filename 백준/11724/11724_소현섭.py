import sys
sys.setrecursionlimit(1000000)

def dfs(v):
    visited[v] = 1
    for i in graph[v]:
        if not visited[i]:
            dfs(i)

n, m = map(int, sys.stdin.readline().split())
visited = [0 for _ in range(n+1)]
graph = [[] for _ in range(n+1)]
answer = 0

for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, n + 1):
    if not visited[i]:
        dfs(i)
        answer += 1
        
print(answer)