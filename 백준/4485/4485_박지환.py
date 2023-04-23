import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)
cnt = 0

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

def dijkstra(graph, x, y):
    min_cost = [[INF]*n for _ in range(n)] # 최소비용

    q = []
    heapq.heappush(q, (graph[x][y], x, y)) # q에 graph, x, y를 모두 넣는다 -> x, y : 시작점
    min_cost[x][y] = graph[x][y] # 시작점의 최소비용 = 시작점의 도둑루피 크기
 
    while q:
        now_cost, x, y = heapq.heappop(q)
    
        for dir in range(4):
            if 0 <= x + dx[dir] < n and 0 <= y + dy[dir] < n:
                cost = now_cost + graph[x + dx[dir]][ y + dy[dir]] # 비용 = 현재비용 + 이동할 칸의 비용

                if cost < min_cost[x + dx[dir]][ y + dy[dir]]: # 비용이 최소비용보다 작을 떄
                    min_cost[x + dx[dir]][ y + dy[dir]] = cost
                    heapq.heappush(q, (cost, x + dx[dir], y + dy[dir]))
        
    return min_cost[n-1][n-1]

while True:
    n = int(input())

    if n == 0:
      break

    graph = [list(map(int, input().split())) for _ in range(n)]
    cnt += 1
    print(f'Problem {cnt}: {dijkstra(graph, 0, 0)}')

    