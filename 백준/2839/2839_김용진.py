# 설탕 배달

import sys
sys.stdin = open('input.txt','r')

num = int(input())
cnt = 0
while 1:   
    if num == 4:
        print(-1)
        break
    if num % 5 == 0:
        cnt += num//5
        print(cnt)
        break
    num -= 3
    cnt += 1