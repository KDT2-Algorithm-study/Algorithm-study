# 유기농 배추
# 소담님 코드 + 유튜브 보고 참고하여 풀었습니다.
import sys
sys.setrecursionlimit(10**6)
sys.stdin = open('input.txt','r')

dx = [0,0,-1,1]
dy = [1,-1, 0,0]

def dfs(x,y):
    global visited
    visited[x][y] = 1
    for i in range(4):
        newX = x + dx[i]
        newY = y + dy[i]
        if 0 <= newX < N and 0 <= newY< M:
            if visited[newX][newY] == 0 and graph[newX][newY] == 1:
                dfs(newX, newY)

T = int(input())
for _ in range(T):
    M,N,K = map(int,input().split())
    graph = [[0] * M for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    for _ in range(K):
        a, b =map(int,input().split())
        graph[b][a] = 1

    answer = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] and  not visited[i][j]:
                dfs(i,j)
                answer += 1


    print(answer)
