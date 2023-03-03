import heapq
import sys

input = sys.stdin.readline

heap = []
num = int(input())


for _ in range(num) :
    i = int(input())

    if i != 0 :
        heapq.heappush(heap, -1*i)
    else :    
        if len(heap) == 0 :
            print (0)
        else :
            print((-1)*heapq.heappop(heap))    