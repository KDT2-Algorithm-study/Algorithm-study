import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)


V, E = map(int, input().split())
start = int(input()) # 시작점
graph = [[] for i in range(V + 1)]
distance = [INF] * (V + 1) # (도착점, 가중치)


for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    
    while q:
        dist, now = heapq.heappop(q) # dist: 최단거리, now: 현재 위치
        if distance[now] < dist: # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
            continue
        for i in graph[now]: # 현재 노드와 연결된 다른 인접한 노드들을 확인
            cost = dist + i[1]
            # print(f'{now} -> {i[0]} : {cost}')
            
            if cost < distance[i[0]]: # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧을 경우
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(start)

for i in range(1, V + 1): # 모든 노드로 가기 위한 최단 거리를 출력
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])



# ---------------------------------------------------------------------------
# 시간 초과(우선순위 큐 사용 안함)


# import sys
# from collections import deque

# V, E = map(int, sys.stdin.readline().split())
# k = int(sys.stdin.readline())
# graph = [[] for _ in range(V+1)]
# weight = [[] for _ in range(V+1)]
# score = [0 for _ in range(V+1)]

# for _ in range(E):
#     u, v, w = map(int, sys.stdin.readline().split())
#     graph[u].append(v)
#     weight[u].append(w)
    
# def dijkstra(k, graph, weight, score):
#     queue = deque([k])
    
#     while queue:
#         n = queue.popleft()
        
#         for i in range(len(graph[n])):
#             if score[graph[n][i]] == 0:
#                 score[graph[n][i]] = score[n] + weight[n][i]
#                 queue.append(graph[n][i])
                
#             elif score[graph[n][i]] > score[n] + weight[n][i]:
#                 score[graph[n][i]] = score[n] + weight[n][i]
#                 queue.append(graph[n][i])


#     for j in range(1, V+1):
#         if j != k and score[j] == 0:
#             print('INF')
#         else:
#             print(score[j])   
    

# dijkstra(k, graph, weight, score)