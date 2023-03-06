# 피보나치 수 5

import sys
sys.stdin = open('input.txt','r')

num = int(input())

lst = [0,1]
cnt = 0

while 1:
    lst.append(lst[cnt] + lst[cnt+1])
    cnt += 1
    if cnt == num:
        lst.pop()
        print(lst[-1])
        break
    else:
        if num == 0:
            print(0)
            break
        elif num == 1:
            print(1)
            break
    