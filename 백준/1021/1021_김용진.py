# 회전하는 큐
import sys
sys.stdin = open('input.txt','r')

from collections import deque

N, M = map(int,input().split())
idx = list(map(int,input().split()))
num = deque()
num_list = []
cnt = 0
t = 0
for i in range(1,N+1):
    num.append(i)

while 1:
    x = idx[t]
    if num.index(x) == 0:
        num_list.append(num.popleft())
        t += 1
        if len(num_list) == M:
            break
    else:
        if num.index(x) < (len(num)/2):
            num.append(num.popleft())
            cnt += 1
        elif num.index(x) > (len(num)/2):
            num.appendleft(num.pop())
            cnt +=1
        elif num.index(x) == (len(num)/2):
            num.appendleft(num.pop())
            cnt += 1
    
print(cnt)
