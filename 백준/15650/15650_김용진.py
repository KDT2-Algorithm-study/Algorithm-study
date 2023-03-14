# N 과 M(2)

import sys
sys.stdin = open('input.txt','r')

result = []
N,M = map(int,input().split())

visited = [False for _ in range(N+1)]

def back(a):
    if a == M:
        print(' '.join(map(str,result)))
        return
    for i in range(1, N+1):
        if not visited[i] and (not result or result[-1] < i):
            result.append(i)
            visited[i] = True
            back(a+1)
            visited[i] = False
            result.pop()
    
back(0)