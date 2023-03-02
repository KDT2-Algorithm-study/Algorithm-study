import heapq
import sys
input = sys.stdin.readline
heap = []

for _ in range(int(input())):
    n = int(input())
    if n == 0:
        if len(heap) > 0:
            print(heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap,n)