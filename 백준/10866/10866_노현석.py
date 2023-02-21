import sys
from collections import deque

deq = deque()
n = int(sys.stdin.readline())

for i in range(n):
    m = list(sys.stdin.readline().split())
    if m[0] =='push_front':
        deq.appendleft(m[1])
    elif m[0] == 'push_back':
        deq.append(m[1])

    elif m[0] == 'pop_front':
        if deq:
            print(deq.popleft())
        else:
            print(-1)
    elif m[0] == 'pop_back':
        if deq:
            print(deq.pop())
        else:
            print(-1)
    elif m[0] == 'size':
        print(len(deq))
    elif m[0] == 'empty':
        if deq:
            print(0)
        else:
            print(1)
    elif m[0] == 'front':
        if deq:
            print(deq[0])
        else:
            print(-1)
    elif m[0] == 'back':
        if deq:
            print(deq[-1])
        else:
            print(-1)
