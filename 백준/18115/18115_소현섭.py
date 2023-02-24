import sys
from collections import deque

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))[::-1]
answer = deque([])

for x, y in zip(a, range(1, n+1)):
    if x == 1:
        answer.appendleft(y)
    elif x == 2:
        answer.insert(1, y)
    elif x == 3:
        answer.append(y)

print(*answer)