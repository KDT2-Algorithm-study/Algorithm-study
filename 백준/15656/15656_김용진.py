# N 과 M (7)

import sys
sys.stdin = open('input.txt','r')

N,M = map(int,input().split())

visited = sorted(list(map(int,input().split())))

result = []
def back(a):
    if a == M:
        print(' '.join(map(str,result)))
        return
    
    for i in range(N):
        result.append(visited[i])
        back(a+1)
        result.pop()

back(0)