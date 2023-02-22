# 2164. 카드 2

import sys
from collections import deque


n = int(sys.stdin.readline())
num_lst = deque([num for num in range(1, n+1)])

while len(num_lst) > 1:
    num_lst.popleft()
    num_lst.append(num_lst.popleft())
    
print(num_lst[0])