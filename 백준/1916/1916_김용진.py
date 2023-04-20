# 최단경로

import sys,heapq
sys.stdin = open('input.txt','r')
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

# 노드의 개수 , 간선의 개수를 입력받기
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for _ in range(n + 1)]

# 방문한 적이 있는지 체크하는 목적의 리스트를 만들기
visited = [False] * (n+1)

# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n+1)

# 모든 간선 정보를 입력받기
for _ in range(m):
    a,b,c = map(int, sys.stdin.readline().split())
    # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    graph[a].append((b,c))
# 시작 노드 번호를 입력받기
b,c = map(int,sys.stdin.readline().split())

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
dijkstra(b)


print(distance[c])