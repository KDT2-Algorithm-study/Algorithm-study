import sys
input= sys.stdin.readline
import heapq
l = []
for _ in range(int(input())):
    a = int(input())
    if a != 0:
        heapq.heappush(l,-a)
    else:
        try: print(heapq.heappop(l)*-1)
        except: print(0)
