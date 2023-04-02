import sys
import heapq

N = int(sys.stdin.readline())
card = [int(sys.stdin.readline()) for _ in range(N)]


heapq.heapify(card)
min = tmp_1 = tmp_2 = 0
tmp = heapq.heappop(card)

while len(card) != 0:
    heapq.heappush(card, tmp)
    tmp = tmp_1 = tmp_2 = 0
    tmp_1 = heapq.heappop(card)
    tmp_2 = heapq.heappop(card)
    tmp = tmp_1 + tmp_2
    min += tmp
    
print(min)