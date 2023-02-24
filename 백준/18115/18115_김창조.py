# 18115. 카드 놓기

import sys
from collections import deque

n = int(input())
cmd_lst = list(map(int, input().split()))

origin_lst = deque()    # as deque
start_lst = [num for num in range(n, 0, -1)]    # as stack

for cmd in cmd_lst[::-1]:
    # 기술 반대로 tracking
    # 바닥에 있는 카드 더미 중 제일 위 카드 손에 들린 카드 더미로 이동
    
    # 손 제일 위에 추가
    if cmd == 1:
        origin_lst.appendleft(start_lst.pop())
    
    # 손 제일 위에서 두번째로 추가
    elif cmd == 2:
        temp = origin_lst.popleft()
        origin_lst.appendleft(start_lst.pop())
        origin_lst.appendleft(temp)
    
    # 손 제일 아래로 추가
    elif cmd == 3:
        origin_lst.append(start_lst.pop())
    
    else:
        sys.exit("Wrong Input")
        
print(*origin_lst)