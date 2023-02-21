# 10866 덱

import sys
from collections import deque


case_num = int(sys.stdin.readline().rstrip())

deq = deque()
for _ in range(case_num):
    cmd = sys.stdin.readline().rstrip()
    
    if "push_front" in cmd:
        deq.appendleft(int(cmd.split()[1]))
    
    elif "push_back" in cmd:
        deq.append(int(cmd.split()[1]))
    
    elif "pop_front" == cmd:
        print(deq.popleft()) if deq else print(-1)
        
    elif "pop_back" == cmd:
        print(deq.pop()) if deq else print(-1)
    
    elif "size" == cmd:
        print(len(deq))
    
    elif "empty" == cmd:
        print(0) if deq else print(1)
    
    elif "front" == cmd:
        print(deq[0]) if deq else print(-1)
    
    elif "back" == cmd:
        print(deq[-1]) if deq else print(-1)
    
    else:
        sys.exit("Wrong Input")