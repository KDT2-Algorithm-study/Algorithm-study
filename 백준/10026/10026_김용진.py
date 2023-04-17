# 적록색약
# 답을 보고 풀었습니다..
import sys
from collections import deque
sys.stdin = open('input.txt','r')


def bfs(x,y):
    q.append((x,y))
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    visited[x][y] = 1
    while q:
        x,y = q.popleft()
        for d in  range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0<=nx<N and 0<=ny<N and color_list[nx][ny] == color_list[x][y] and not visited[nx][ny]: # 범위 안에서 and 같은 색이면서 and 방문 안한 경우
                visited[nx][ny] = 1
                q.append((nx,ny))

N = int(input())
color_list = [list(input()) for _ in range(N)]
q = deque()


visited = [[0]*N for _ in range(N)]
cnt1 = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i,j)
            cnt1 += 1


for i in range(N):
    for j in range(N):
        if color_list[i][j] == 'G':
            color_list[i][j] = 'R'


visited = [[0]*N for _ in range(N)]
cnt2 = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i,j)
            cnt2 += 1

print(cnt1,cnt2)
