# 1260. DFS와 BFS

from sys import stdin
from collections import deque

n, m, start = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    v1, v2 = map(int, stdin.readline().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

for i in range(1, n+1):
    graph[i] = sorted(graph[i])
    

# fail
def dfs_loop(start: int):
    answer = list()
    
    UNVISITED = 0
    CHECKED = 1
    VISITED = 2
    
    n = len(graph) - 1
    visited = [UNVISITED] * (n+1)
    stack = [start]
    
    next = 0
    while len(answer) < n and stack:
        v = next if next else stack.pop()
        visited[v] = VISITED
        next = 0
        answer.append(v)
        for idx, adj in enumerate(graph[v][-1::-1]):
            if visited[adj] == CHECKED:
                next = adj
            elif not visited[adj]:
                stack.append(adj)
                visited[adj] = CHECKED
    
    print(' '.join(map(str, answer)))
    
    
def dfs_recursion(v: int):
    answer.append(v)
    for adj in graph[v]:
        if not visited[adj]:
            visited[adj] = True
            dfs_recursion(adj)
    
        
def bfs(start: int):
    answer = list()
    
    n = len(graph) - 1
    visited = [False] * (n+1)
    deq = deque([start])
    
    visited[start] = True
    while deq:
        v = deq.popleft()
        answer.append(v)
        for adj in graph[v]:
            if not visited[adj]:
                deq.append(adj)
                visited[adj] = True
    
    print(' '.join(map(str, answer)))
    
    
# variable for dfs
answer = list()
visited = [False] * (n+1)
visited[start] = True
dfs_recursion(start)
print(' '.join(map(str, answer)))

bfs(start)