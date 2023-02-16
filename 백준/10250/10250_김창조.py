# 10250 ACM 호텔

import sys

test_case = int(sys.stdin.readline().rstrip())
for T in range(test_case):
    height, width, order = map(int, sys.stdin.readline().rstrip().split())
    
    room = str((order-1)%height+1) + f"{(order-1)//height+1:02d}"
    print(room)