from collections import deque

def dfs(k):

    visited_dfs[k] = True
    print(k, end=' ')

    for i in range(1, n + 1):
        if not visited_dfs[i] and graph[k][i]:
            dfs(i)

def bfs(k):
    q = deque()
    q.append(k)
    visited_bfs[k] = True

    while q:
        v = q.popleft()
        print(v, end=' ')

        for i in range(1, n+1):
            if not visited_bfs[i] and graph[v][i]:
                q.append(i)
                visited_bfs[i] = True

n, m, k = map(int , input().split())
graph = [[False] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = True

visited_dfs = [False for _ in range(n+1)]
visited_bfs = [False for _ in range(n+1)]

dfs(k)
print()
bfs(k)