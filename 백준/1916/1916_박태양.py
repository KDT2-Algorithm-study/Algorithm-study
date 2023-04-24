import heapq
n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for i in range(m):
    ss, es, cost = map(int,input().split())
    graph[ss].append((es,cost))
start,end = map(int,input().split())

costlst = [100000*100000]*(n+1)

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    costlst[start] = 0
    while q:
        c, n = heapq.heappop(q)
        if costlst[n]< c:
            continue
        for i in graph[n]:
            cost = c + i[1]
            if cost < costlst[i[0]]:
                costlst[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

print(costlst[end])
