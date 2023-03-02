# 1927. 최소 힙

import sys
import heapq

n = int(sys.stdin.readline())

q = []
for _ in range(n):
    x = int(sys.stdin.readline())
    if x == 0:
        if q:
            print(heapq.heappop(q))
        else:
            print(0)
    else:
        heapq.heappush(q, x)