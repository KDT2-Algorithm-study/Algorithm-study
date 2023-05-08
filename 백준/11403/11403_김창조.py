# 11403. 경로 찾기

import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
G = [list(map(int, input().split())) for _ in range(N)]
answer = [[0] * N for _ in range(N)]

def bfs(start: int):
    global G, N, answer
    q = deque([start])
    visited = [False] * N
    
    while q:
        v = q.popleft()
        for idx, flag in enumerate(G[v]):
            if flag and not visited[idx]:
                answer[start][idx] = 1
                visited[idx] = True
                q.append(idx)

for i in range(N):
    bfs(i)
    
for line in answer:
    print(' '.join(map(str, line)))