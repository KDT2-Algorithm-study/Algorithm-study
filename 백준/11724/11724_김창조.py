# 11724. 연결 요소의 개수

import sys
from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    v1, v2 = map(int, sys.stdin.readline().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

answer = 0

for i in range(1, n+1):
    if visited[i]:
        continue
    
    answer += 1
    deq = deque([i])
    visited[i] = True
    # bfs
    while deq:
        v = deq.popleft()
        for adj in graph[v]:
            if not visited[adj]:
                visited[adj] = True
                deq.append(adj)
                
print(answer)