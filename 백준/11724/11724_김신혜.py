
import sys
from pprint import pprint
N, E = map(int, sys.stdin.readline().split())
graph = [ [] for _ in range(N+1)]
visited = []
# visited = [False] * (N+1)
cnt = 0

def dfs(n):
    visited.append(n)
    for n in graph[n]:
        if n not in visited:
            dfs(n)

for _ in range(E):
    u, v = map(int, sys.stdin.readline().split()) 
    graph[u].append(v)
    graph[v].append(u)
# pprint(graph)


for n in range(1, N+1): 
    if n not in visited:
        # while True:
        #     visited.append(n)
        #     for i in graph[n]:
        #         if i not in visited:
        #             visited.append(n)
        #         elif i == graph[n][-1]:
        #             print(graph[n][-1])
        #             break
        dfs(n)
        cnt += 1
print(cnt)
