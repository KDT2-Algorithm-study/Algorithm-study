# 1916. 최소비용 구하기

import sys
import heapq

N = int(input())
M = int(input())
distance = [int(1e9)] * N
graph = [[] for _ in range(N)]

for _ in range(M):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u-1].append((v-1, w))
    
start, destination = map(int, input().split())


def dijkstra(start: int):
    global graph, distance
    
    q = list()
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        cur_cost, cur_city = heapq.heappop(q)
        
        if cur_cost > distance[cur_city]:
            continue
        
        for city, cost in graph[cur_city]:
            new_distance = distance[cur_city] + cost
            if distance[city] > new_distance:
                distance[city] = new_distance
                heapq.heappush(q, (distance[city], city))


dijkstra(start-1)
print(distance[destination-1])