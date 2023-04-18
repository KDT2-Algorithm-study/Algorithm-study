# 1417. 국회의원 선거

import sys
import heapq

n = int(input())
vote = int(input())
origin = vote
q= list()
for _ in range(n-1):
    num = int(sys.stdin.readline())
    if num >= vote:
        # votes.append(num)
        heapq.heappush(q, -num)

while q:
    first = heapq.heappop(q)
    first *= -1
    if first < vote:
        break
    first -= 1
    vote += 1
    heapq.heappush(q, -first)
    
print(vote - origin)