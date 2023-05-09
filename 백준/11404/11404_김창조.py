# 11404. 플로이드

import sys
import heapq
input = sys.stdin.readline
inf = int(1e9)

n = int(input())
m = int(input())
answer = [[inf] * n for _ in range(n)]

    
def solution_dijkstra():
    global n, answer
    
    G = [[] for _ in range(n)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        G[a-1].append([b-1, c])
        
    for idx in range(n):
        q = [[0, idx]]
    
        while q:
            cur_cost, cur = heapq.heappop(q)
            if cur_cost > answer[idx][cur]:
                continue
            
            for adj, adj_cost in G[cur]:
                cost = cur_cost + adj_cost
                if answer[idx][adj] > cost:
                    answer[idx][adj] = cost
                    heapq.heappush(q, [cost, adj])
            
                    
        for i, num in enumerate(answer[idx]):
            if num == inf:
                answer[idx][i] = 0
        answer[idx][idx] = 0
        print(' '.join(map(str, answer[idx])))
    
        
        
def solution_floyd():
    global n, answer
    
    G = [[inf]*n for _ in range(n)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        # 시작 도시와 도착 도시를 연결하는 노선은 하나가 아닐 수 있다.
        if c < G[a-1][b-1]:
            G[a-1][b-1] = c
      
    answer = G.copy()
    for i in range(n):
        answer[i][i] = 0
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                answer[i][j] = min(answer[i][j], answer[i][k] + answer[k][j])
        
    for line in answer:
        for i, num in enumerate(line):
            if num == inf:
                line[i] = 0
        print(' '.join(map(str,line)))

# solution_dijkstra()
solution_floyd()