# 2167. 2차원 배열의 합

import sys


input = sys.stdin.readline

N, M = map(int, input().split())

lst = []
for i in range(N):
    line = list(map(int, input().split()))
    for idx, num in enumerate(line):
        if idx:
            line[idx] = line[idx-1] + num
    lst.append(line)
    
K = int(input())

for _ in range(K):
    answer = 0
    i, j, x, y = map(int, input().split())
    for p in range(i-1, x):
        answer += lst[p][y-1]
        if j > 1:
            answer -= lst[p][j-2]
          
    print(answer)