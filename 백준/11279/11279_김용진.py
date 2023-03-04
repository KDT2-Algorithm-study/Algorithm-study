# 최대 힙
import sys,heapq
sys.stdin = open('input.txt','r')

T = int(sys.stdin.readline())
a = []
b = []
for t in range(T):
    num = int(sys.stdin.readline())
    b.append(num)
for i in b:
    if i != 0:
        heapq.heappush(a,-i)
    else:
        if len(a) != 0:
            print(-heapq.heappop(a))
        else:
            print(0)
