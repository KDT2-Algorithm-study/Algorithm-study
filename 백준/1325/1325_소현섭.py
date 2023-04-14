import sys
from collections import deque

def bfs(start):
    queue = deque()
    queue.append(start)
    visited = [0]*(N+1)
    visited[start] = 1
    while queue:
        X = queue.popleft()
        for Y in graph[X]:
            if visited[Y] == 0:
                visited[Y] = 1
                queue.append(Y)
    return sum(visited)


N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
answer = []
max_num = 0

for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())
    graph[y].append(x)

for start in range(1, N+1):
    x = bfs(start)
    if max_num < x:
        answer = [start]
        max_num = x
    elif max_num == x:
        answer.append(start)

print(*answer)