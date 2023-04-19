# 슈퍼 마리오

import sys
sys.stdin = open('input.txt','r')
cnt = 0
a = []
for _ in range(10):
    num = int(input())
    cnt += num
    a.append(num)

    if cnt >= 100:
        d = a.pop()
        b = cnt - 100
        c = 100 - (cnt-d)
        if b > c:
            print(cnt-d)
            break
        else:
            print(cnt)
            break
else:
    print(cnt)
    

