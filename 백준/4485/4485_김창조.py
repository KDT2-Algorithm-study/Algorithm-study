# 4485. 녹색 옷 입은 애가 젤다지?

import sys
import heapq

test_case = 0
DELTA = [(0, 1), (0, -1), (1, 0), (-1, 0)]

while True:
    test_case += 1
    N = int(sys.stdin.readline())
    if N == 0:
        break
    
    map_ = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    cost = [[int(1e9)] * N for _ in range(N)]

    q = []
    heapq.heappush(q, (map_[0][0], 0, 0))
    
    while q:
        cur_cost, y, x = heapq.heappop(q)
        
        if y == N-1 and x == N-1:
            answer = cur_cost
            break
        
        for dy, dx in DELTA:
            ny, nx = y + dy, x + dx
            if not (0 <= ny < N and 0 <= nx < N):
                continue
            new_cost =  map_[ny][nx] + cur_cost
            if cost[ny][nx] > new_cost:
                cost[ny][nx] = new_cost
                heapq.heappush(q, (new_cost, ny, nx))

    print(f'Problem {test_case}: {answer}')