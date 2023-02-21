import sys
from collections import deque
queue = deque()
N = int(sys.stdin.readline())

for i in range(N):
    commend = list(sys.stdin.readline().split())
    if commend[0] == 'push_front':
        queue.appendleft(int(commend[1]))

    elif commend[0] == 'push_back':
        queue.append(int(commend[1]))

    elif commend[0] == 'pop_front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())

    elif commend[0] == 'pop_back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.pop())

    elif commend[0] == 'size':
        print(len(queue))

    elif commend[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)

    elif commend[0] == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])

    elif commend[0] == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])