import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
visited = [0]*(n+1)
queue = deque()
answer = 0

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for j in range(1, n+1): # bfs
    if visited[j] == 0:
        visited[j] = 1
        answer += 1
        queue.append(j)

        while queue:
            q = queue.popleft()
            for k in graph[q]:
                if visited[k] == 0:
                    visited[k] = 1
                    queue.append(k)

print(answer)

#========================================================

# for i in range(1, n+1): # dfs
#     if visited[i] == 0: 
#         visited[i] = 1
#         answer += 1
#         stack = [i]
        
#         while stack:
#             p = stack.pop()
#             for j in graph[p]:
#                 if visited[j] == 0:
#                     visited[j] = 1
#                     stack.append(j)
# 
# print(answer)
