# 지그재그 숫자

import sys
sys.stdin = open('input.txt','r')

T = int(input())

for t in range(1,T+1):
    cnt = 0
    num = int(input())
    for i in range(1,num+1):
        if i % 2 != 0:
            cnt += i
        else:
            cnt -= i
    print(f'#{t} {cnt}')