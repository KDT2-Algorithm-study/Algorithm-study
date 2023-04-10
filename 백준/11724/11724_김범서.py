from collections import deque

def bfs(start):
    que = deque([start])
    while que:
        now = que.popleft()
        if not visited[now]:
            visited[now] = True
            for point in linked[now]:
                if not visited[point]:
                    que.append(point)

n, m = map(int, input().split())
linked = [[] for i in range(n + 1)]
visited = [True] + [False] * n
que = deque([])
result = 0

for i in range(m):
    u, v = map(int, input().split())
    linked[u].append(v)
    linked[v].append(u)

for i in range(1, n + 1):
    if not visited[i]:
        bfs(i)
        result += 1

print(result)
