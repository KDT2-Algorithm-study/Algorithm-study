# 요세푸스 문제0

from collections import deque
import sys
sys.stdin = open('input.txt','r')

n, k = map(int,input().split())
a = deque([])
b = []
for i in range(1,n+1):
    a.append(i)
print('<', end ='')
while len(a) != 0:
    for x in range(k-1):
        a.append(a[0])
        a.popleft()
    print(a.popleft(), end='')
    if a:
        print(',',end =' ')
print('>')