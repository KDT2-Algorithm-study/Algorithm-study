# 1753. 최단경로

import sys
from collections import deque
import heapq
from pprint import pprint

V, E = map(int, input().split())
K = int(input())
graph = [[] for _ in range(V)]
# answer = [float('inf')] * V
INF = sys.maxsize
answer = [INF] * V

for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split()) 
    graph[u-1].append((v-1, w))

# Time over
def bfs(start: int):
    global graph, answer
    
    deq = deque([start])
    
    while deq:
        cur = deq.popleft()
        for adj, weight in graph[cur]:
            if not weight:
                continue
            if cur == start or not answer[adj] or answer[adj] > answer[cur] + weight:
                answer[adj] = answer[cur] + weight
                deq.append(adj)
                
                
def dijkstra(start: int):
    global graph, answer
    
    q = list()
    answer[start] = 0
    heapq.heappush(q, (0, start))
    
    while q:
        cur_weight, cur_node = heapq.heappop(q)
        if cur_weight > answer[cur_node]:
            continue
        
        for adj, weight in graph[cur_node]:
            if answer[adj] > cur_weight + weight:
                answer[adj] = cur_weight + weight
                heapq.heappush(q, (answer[adj], adj))
    

# bfs(K-1)
dijkstra(K-1)
for goal in range(V):
    if answer[goal] == INF:
        print('INF')
    else:
        print(answer[goal])