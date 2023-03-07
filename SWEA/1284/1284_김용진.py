# 수도 요금 경쟁

import sys
sys.stdin = open('input.txt','r')

T = int(input())

for t in range(1,T+1):
    P,Q,R,S,W = map(int,input().split())

    num1 = P * W

    if R > W:
        num2 = Q
    else:
        num2 = Q + ((W-R) * S)

    if num1 > num2:
        print(f'#{t} {num2}')
    else:
        print(f'#{t} {num1}')