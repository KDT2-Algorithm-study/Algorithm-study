import sys
from collections import deque

dq = deque([])

for _ in range(int(sys.stdin.readline())):
    command = sys.stdin.readline().rstrip()
    if 'push_front' in command:
        dq.appendleft(command.split()[1])
    elif 'push_back' in command:
        dq.append(command.split()[1])
    elif 'pop_front' == command:
        if not dq:
            print('-1')
        else:
            print(dq.popleft())
    elif 'pop_back' == command:
        if not dq:
            print('-1')
        else:
            print(dq.pop())
    elif 'size' == command:
        print(len(dq))
    elif 'empty' == command:
        if not dq:
            print('1')
        else:
            print('0')
    elif 'front' == command:
        if not dq:
            print('-1')
        else:
            print(dq[0])
    elif 'back' == command:
        if not dq:
            print('-1')
        else:
            print(dq[-1])