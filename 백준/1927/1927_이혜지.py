import heapq
import sys

input= sys.stdin.readline

num = int(input())
heap = []

for _ in range(num) :
    i = int(input())

    if i == 0 :
        if len(heap) != 0 :
            print(heapq.heappop(heap))
        else :
            print(0)    
    else :
        heapq.heappush(heap, i)        