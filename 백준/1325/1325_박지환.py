import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

# def dfs(start):
#     cnt = 1
#     stack = [start]
#     visit = [0 for _ in range(n+1)]
#     visit[start] = 1

#     while stack:
#         v = stack.pop()

#         for i in graph[v]:
#             if not visit[i]:
#                 visit[i] = 1
#                 cnt += 1
#                 stack.append(i)
    
#     return cnt


def bfs(start):
    cnt = 1
    queue = deque([start])
    visit = [0 for _ in range(n+1)]
    visit[start] = 1

    while queue:
        v = queue.popleft()

        for i in graph[v]:
            if not visit[i]:
                visit[i] = 1
                cnt += 1
                queue.append(i)
    
    return cnt


graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[b].append(a)

max_cnt = 1 # 컴퓨터 1대를 해킹했을 시 최대 몇 대의 컴퓨터를 해킹할 수 있는지 찾는 문제
ans = []

for j in range(1, n+1):
    # cnt = dfs(j)
    cnt = bfs(j)

    if cnt > max_cnt: # cnt 가 최댓값보다 큰 경우
        max_cnt = cnt
        ans.clear() # 이제까지의 컴퓨터 정보를 지움
        ans.append(j)
        
    elif cnt == max_cnt: # cnt 가 최댓값과 같은 경우
        ans.append(j) # 이제까지의 컴퓨터 정보에 추가

print(*ans)