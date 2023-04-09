# DFS 와 BFS

import sys
sys.stdin = open('input.txt','r')

def dfs(a):
    global visted
    visted[a] = True
    print(a, end=' ')
    for next in range(1,N+1):
        if not visted[next] and graph[a][next]:
            dfs(next)

def bfs(a):
    global q,visted
    while q:
        cur = q.pop(0)
        print(cur,end = ' ')
        for next in range(1,N+1):
            if not visted[next] and graph[cur][next]:
                visted[next] = True
                q.append(next)

N, M, V = map(int,input().split()) 

graph = [[0] *(N+1) for _ in range(N+1)] 
visted =[0] * (N+1)


for _ in range(M):
    a, b = map(int,input().split())
    graph[a][b] = 1 
    graph[b][a] = 1


dfs(V)
print()


visted = [False] * (N+1)
q = [V]
visted[V] = True

bfs(V)


