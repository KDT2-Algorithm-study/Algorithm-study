import sys
import heapq

input = sys.stdin.readline
num = []
cnt = 0
for i in range(int(input())):
    heapq.heappush(num,int(input()))

while len(num) != 1:
    a = heapq.heappop(num)
    b = heapq.heappop(num)
    heapq.heappush(num,a+b)
    cnt += (a+b)
print(cnt)