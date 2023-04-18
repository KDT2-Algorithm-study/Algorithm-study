# 국회의원 선거

import sys,heapq
sys.stdin = open('input.txt','r')

T = int(input())
a = int(input())
b = []
cnt = 0
for t in range(T-1):
    heapq.heappush(b,-int(input()))

while 1:
    if len(b) == 0:
        break
    c = -heapq.heappop(b)
    if a <= c :
        a += 1
        cnt += 1
        heapq.heappush(b,-(c-1))
    else:
        break

print(cnt)