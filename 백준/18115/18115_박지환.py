import sys
from collections import deque

n = int(sys.stdin.readline())
skills = list(map(int, sys.stdin.readline().split()))
nums = deque(range(1, n+1))
queue = deque()

while nums:
    t = skills.pop()
    
    if t == 1:
        queue.appendleft(nums.popleft())
    
    elif t == 2:
        tmp = queue.popleft()
        queue.appendleft(nums.popleft())
        queue.appendleft(tmp)
    
    else:
        queue.append(nums.popleft())

print(*queue)