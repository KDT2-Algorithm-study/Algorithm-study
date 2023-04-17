import sys
import heapq

sys.setrecursionlimit(10**6)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for x in graph[now]:
            cost = dist + x[1]
            if cost < distance[x[0]]:
                distance[x[0]] = cost
                heapq.heappush(q, (cost, x[0]))

V, E = map(int, sys.stdin.readline().split())
k = int(sys.stdin.readline())
INF = int(1e9)
graph = [[] * (V+1) for _ in range(V+1)]
distance = [INF] * (V+1)

for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((v, w))

dijkstra(k)

for y in range(1, V+1):
    if distance[y] == INF:
        print("INF")
    else:
        print(distance[y])