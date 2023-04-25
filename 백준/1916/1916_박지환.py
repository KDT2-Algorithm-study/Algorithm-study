import sys
import heapq
input = sys.stdin.readline
INF = (1e9)

n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
cost_list = [INF]*(n + 1)

for _ in range(m):
    d, a, c = map(int, input().split())
    graph[d].append((a, c))
    
start, end = map(int, input().split())    

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    
    while q:
        now_cost, now = heapq.heappop(q)
        if  cost_list[now] < now_cost:
            continue
        for i in graph[now]:
            cost = now_cost + i[1]
            
            if cost < cost_list[i[0]]:
                cost_list[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    return cost_list[end]

print(dijkstra(start))