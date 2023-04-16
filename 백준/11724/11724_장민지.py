# 11724 연결 요소의 개수
import sys
n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)
visited = [False] * (n+1)
visited[0] = [True]
cnt = 0
for a in range(1, n+1):
    stack = [a]
    if visited[a] == False:
        while stack:
            cur = stack.pop()
            for i in graph[cur]:
                if visited[i] == False:
                    visited[i] = True
                    stack.append(i)
        cnt += 1
print(cnt)