from collections import deque
import sys

input = sys.stdin.readline

def bfs(start):
  queue = deque()
  queue.append(start)       
  visit_list[start] = 1   
  while queue:
    start = queue.popleft()
    BFS.append(start)
    for i in range(1, n + 1):
      if visit_list[i] == 0 and graph[start][i] == 1:
        queue.append(i)
        visit_list[i] = 1

def dfs(start):
  visit_list[start] = 1        
  DFS.append(start)
  for i in range(1, n + 1):
    if visit_list[i] == 0 and graph[start][i] == 1:
      dfs(i)

n, m, num = map(int, input().split())
DFS = []
BFS = []

graph = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
  a, b = map(int, input().split())
  graph[a][b] = graph[b][a] = 1

visit_list = [0] * (n + 1)
dfs(num)
visit_list = [0] * (n + 1)
bfs(num)
print(*DFS)
print(*BFS)