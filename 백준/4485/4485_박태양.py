import heapq
import sys
input = sys.stdin.readline

d = [(1,0),(-1,0),(0,1),(0,-1)]
INF = 125*125*9
cnt = 1
def dijkstra(graph,result_graph,num):
    q = []

    heapq.heappush(q,(graph[0][0],0,0))
    result_graph[0][0] = graph[0][0]
    while q:
        c, x, y = heapq.heappop(q)
        for dx,dy in d:
            if 0 <= x+dx < num and 0 <= y+dy < num :
                new_c = c + graph[y+dy][x+dx] 

                if new_c < result_graph[y+dy][x+dx]:
                    result_graph[y+dy][x+dx] = new_c
                    heapq.heappush(q, (new_c, x+dx, y+dy))


while True:
    num = int(input())
    if num == 0:
        break
    
    cost = [[] for _ in range(num)]
    for i in range(num):
        cost[i] = list(map(int,input().split()))
    
    min_cost = [[INF]*num for _ in range(num)]

    dijkstra(cost,min_cost,num)

    print(f'Problem {cnt}: {min_cost[-1][-1]}')
    cnt +=1