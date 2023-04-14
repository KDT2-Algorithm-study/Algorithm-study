import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(v):
    if visited[v] > 0:
        return
    
    visited[v] = 1
    for i in link[v]:
        dfs(i)

n,m = map(int,input().split())
visited = [0] * n

link = [[] for i in range(n)]
for _ in range(m):
    a,b = map(int,input().split())
    link[a-1].append(b-1)
    link[b-1].append(a-1)

r = 0
for i in range(n):
    if visited[i] == 0:
        r += 1
        dfs(i)
        
print(r)