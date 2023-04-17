# 최단경로
# 책 내용 + 유튜브 내용을 보며 작성해 보았습니다.

import sys,heapq
sys.stdin = open('input.txt','r')
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

# 노드의 개수 , 간선의 개수를 입력받기
n, m = map(int,input().split())

# 시작 노드 번호를 입력받기
start = int(input())

# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for _ in range(n + 1)]

# 방문한 적이 있는지 체크하는 목적의 리스트를 만들기
visited = [False] * (n+1)

# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n+1)

# 모든 간선 정보를 입력받기
for _ in range(m):
    a,b,c = map(int, input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    graph[a].append((b,c))

# heapq를 사용한 다익스트라
def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 거리는 0으로 설정하여, 큐에 삽임
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q : # q가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

# 다익스트라 알고리즘을 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단거리를 출력
for i in range(1, n+1):
    # 도달할 수 없는 경우, 무한(INF)이라고 출력
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])


# # 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환
# def get_smallest_node():
#     min_value = INF
#     index = 0 # 가장 최단 거리가 짧은 노드(인덱스)
#     for i in range(1, n+1):
#         if distance[i] < min_value and not visited[i]:
#             min_value = distance[i]
#             index = i
#         return index
    

# def dijkstra(start):
#     # 시작 노드에 대해서 초기화
#     distance[start] = 0 
#     visited[start] = True
#     for j in graph[start]:
#         distance[j[0]] = j[1]
#     # 시작 노드를 제외한 전체 n-1 개의 노드에 대해 반복
#     for i in range(n-1):
#         # 현재 최단 거리가 가장 짧은 노드를 꺼내서, 방문 처리
#         now = get_smallest_node()
#         visited[now]=True
#         # 현재 노드와 연결된 다른 노드를 확인
#         for j in graph[now]:
#             cost = distance(now)
#             # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
#             if cost < distance[j[0]]:
#                 distance[j[0]] = cost
# # 다익스트라 알고리즘을 수행
# dijkstra(start)

# 모든 노드로 가기 위한 최단거리를 출력
# for i in range(1, n+1):
#     # 도달할 수 없는 경우, 무한(INFINITY)이라고 출력
#     if distance[i] == INF:
#         print('INF')
#     else:
#         print(distance[i])
