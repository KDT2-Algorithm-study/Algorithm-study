# 1325. 효율적인 해킹

import sys
from collections import deque

answer = []
n, m = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    v1, v2 = map(int, sys.stdin.readline().split())
    graph[v2].append(v1)
    
max_cnt = 0
for i in range(1, n+1):
    cnt = 0
    deq = deque([i])
    visited = [False] * (n+1)
    visited[i] = True
    while deq:
        v = deq.popleft()
        cnt += 1
        for adj in graph[v]:
            if not visited[adj]:
                visited[adj] = True
                deq.append(adj)
    
    if cnt > max_cnt:
        max_cnt = cnt
        answer = [i]
    elif cnt == max_cnt:
        answer.append(i)

sys.stdout.write(' '.join(map(str, answer)))