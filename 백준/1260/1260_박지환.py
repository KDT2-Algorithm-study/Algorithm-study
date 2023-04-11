from collections import deque
import sys

# BFS 메서드 정의
def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')
        
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


# DFS 메서드 정의
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end = ' ')

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
n, m, v = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[b].append(a)
    graph[a].append(b)

for j in range(1, n+1):
    graph[j] = sorted(graph[j])


# 각 노드가 방문된 정보를 자료형으로 표현(1차원 리스트)
visited_DFS = [False] * (n+1)
visited_BFS = [False] * (n+1)

# 정의된 DFS 함수 호출
dfs(graph, v, visited_DFS)

print('')
# 정의된 BFS 함수 호출
bfs(graph, v, visited_BFS)
