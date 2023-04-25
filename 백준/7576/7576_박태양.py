import sys
input = sys.stdin.readline
from collections import deque
a,b= map(int,input().split())
l = []
day = 0
for _ in range(b):
    l.append(list(map(int,input().split())))
d = [(0,1),(0,-1),(1,0),(-1,0)]
def bfs():
    global day
    deq = deque()
    for i in range(b):
        for j in range(a):
            if l[i][j] == 1:
                deq.append((j,i,0))
    while deq:
        x,y,cnt = deq.popleft()
        if day<cnt:
            day = cnt
        for dx,dy in d:
            mx = x+dx
            my = y+dy
            if 0<=mx<a and 0<=my<b and l[my][mx] == 0:
                l[my][mx] = 1
                deq.append((mx,my,cnt+1))
    for i in range(b):
        for j in range(a):
            if l[i][j] == 0:
                return -1
    else:
        return day


print(bfs())