import heapq
import sys

n = int(sys.stdin.readline())
command = [int(sys.stdin.readline()) for _ in range(n)]
heap = []

for i in command:
    if i == 0:
        if len(heap) != 0:
            print(heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap, i)
 