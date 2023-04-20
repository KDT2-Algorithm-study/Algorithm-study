import sys
import heapq

def dijkstra(graph, start):
    distances = [int(1e9)] * (N+1)
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [distances[start], start])
    while queue:
        dist, node = heapq.heappop(queue)
        if distances[node] < dist:
            continue
        for next_node, next_dist in graph[node]:
            distance = dist + next_dist
            if distance < distances[next_node]:
                distances[next_node] = distance
                heapq.heappush(queue, [distance, next_node])
    return distances

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))
start, end = map(int, sys.stdin.readline().split())
dist_start = dijkstra(graph, start)
print(dist_start[end])