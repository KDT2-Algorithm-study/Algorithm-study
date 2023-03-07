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

# 재귀함수 사용

# def fibo(m):
#     if m == 0:
#         return 0
#     elif m == 1:
#         return 1
#     else:
#         return fibo(m-1) + fibo (m-2)

# n = int(input())

# ans = fibo(n)
# print(ans)
    