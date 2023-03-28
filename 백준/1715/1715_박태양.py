import heapq
import sys
input = sys.stdin.readline
num = int(input())
heap = []
heapq.heapify(heap)
for _ in range(num):
    heapq.heappush(heap,int(input()))
total = 0
while len(heap)>1:
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    total += a+b
    heapq.heappush(heap,a+b)

print(total)