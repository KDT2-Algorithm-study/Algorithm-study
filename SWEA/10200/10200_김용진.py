# 구독자 전쟁

import sys
sys.stdin = open('input.txt','r')

T = int(input())

for t in range(1,T+1):
    N,A,B = map(int,input().split())
    min_num = min(A,B)
    if N > A+B:
        num = 0
    else:
        num = A+B-N
    
    print(f'#{t} {min_num} {num}')