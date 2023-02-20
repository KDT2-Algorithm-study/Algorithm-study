# N과 M(1)

import sys
sys.stdin = open('input.txt','r')

N,M = map(int,input().split())
result = []
visited = [False for _ in range(N+1)]

def back(num):
    if num == M:
        print(' '.join(map(str,result)))
        return
    for i in range(1,N+1):
        if not visited[i]:
            visited[i] = True
            result.append(i)
            back(num+1)
            visited[i] = False
            result.pop()
back(0)


# 찾아보니 파이썬 내장함수로도 가능하다고 합니다!

# from itertools import permutations
# n, m = map(int, input().split())
# for i in permutations(range(1, n+1), m):
#     print(" ".join(map(str, i)))