# 카드 놓기
import sys
sys.stdin = open('input.txt','r')
from collections import deque

T = int(input())
num = list(map(int,input().split()))
b = deque()
for x in range(1,T+1):
    a = num.pop()
    if a == 1:
        b.appendleft(x)
    elif a == 2:
        b.insert(1, x)
    elif a == 3:
        b.append(x)
print(*b)
        






