import sys
import heapq
h = []
N = int(sys.stdin.readline())
for _ in range(N):
    x = int(sys.stdin.readline())
    if x == 0:
        if h:
            print(-heapq.heappop(h))
        else:
            print(0)
    elif x//1 == x:
        heapq.heappush(h, -x)