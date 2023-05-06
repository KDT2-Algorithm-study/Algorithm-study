# 1009. 분산처리

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    a %= 10
    if a == 0:
        # Num 10
        print(10)
    elif a == 2 or a == 3 or a == 7 or a == 8:
        # Num 2, 3, 7, 8
        # 2, 4, 8, 6, 2, ...
        # 3, 9, 7, 1, 3, ...
        # 7, 9, 3, 1, 7, ...
        # 8, 4, 2, 6, 8, ...
        print(pow(a, (b-1)%4+1) % 10)
    elif a == 4 or a == 9:
        # Num 4, 9
        # 4, 6, 4, ...
        # 9, 1, 9, ...
        print(pow(a, (b-1)%2+1) % 10)
    else:
        # Num 1, 5, 6
        print(a)