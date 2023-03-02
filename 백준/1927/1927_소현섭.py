import sys
import heapq

heap = []
for _ in range(int(sys.stdin.readline())):
    num = int(sys.stdin.readline())
    if num == 0 and not heap:
        print(0)
    elif num != 0:
        heapq.heappush(heap, num)
    elif num == 0:
        print(heapq.heappop(heap))