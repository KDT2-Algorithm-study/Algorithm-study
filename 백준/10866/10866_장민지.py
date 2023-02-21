import sys
from collections import deque
stack = deque()

N = int(input())
for _ in range(N):
    string = sys.stdin.readline().split()
    
    if "push_front" in string:
        stack.appendleft(string[1])

    elif "push_back" in string:
        stack.append(string[1])
    
    elif "pop_front" == string[0]:
        if stack:
            print(stack.popleft())
        else:
            print(-1)
    elif "pop_back" == string[0]:
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif "size" == string[0]:
        print(len(stack))

    elif "empty" == string[0]:
        if stack:
            print(0)
        else:
            print(1)
    elif "front" == string[0]:
        if stack:
            print(stack[0])
        else:
            print(-1)
    elif "back" == string[0]:
        if stack:
            print(stack[-1])
        else:
            print(-1)
