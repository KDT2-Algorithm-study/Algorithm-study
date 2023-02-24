import sys
from collections import deque

n = int(input())
deq = deque()
result = deque(range(1, n+1))

skill = list(sys.stdin.readline().split())

for i in reversed(skill):
    p = result.popleft()
    if i == '1':
        deq.appendleft(p)
    elif i == '2':
        deq.insert(1, p)
    else:
        deq.append(p)

print(*deq)