import sys
from collections import deque

n = int(sys.stdin.readline())
deq = deque()
for i in range(1, n+1):
    deq.append(i)

while len(deq) != 1:
    deq.popleft()
    deq.rotate(-1)
print(*deq)