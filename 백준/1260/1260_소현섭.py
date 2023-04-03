def DFS(v):
    visited[v]=1
    dfs.append(v)
    for i in graph[v]:
        if (visited[i]==0):
            DFS(i)

def BFS(v):
    visited[v]=1
    bfs.append(v)
    queue = [v]

    while(queue):
        for i in graph[queue.pop(0)]:
            if(visited[i]==0):
                visited[i]=1
                bfs.append(i)
                queue.append(i)

N, M, V = map(int, input().split())
graph =[[] for _ in range(N+1)]
visited = [0]*(N+1)
dfs = []
bfs = []

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for x in range(N+1):
    graph[x].sort()

DFS(V)
visited = [0]*(N+1)
BFS(V)

print(*dfs)
print(*bfs)