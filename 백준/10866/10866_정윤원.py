import sys
input = sys.stdin.readline
from collections import deque
N = int(input())
queue = deque()
for i in range(N) :
    command = input().rstrip()
    if command[-1].isdigit() :
        word, num = command.split()
        num = int(num)
        if word == 'push_front' :  queue.appendleft(num)
        elif word == 'push_back' : queue.append(num)
    elif command == 'pop_front' :  print(queue.popleft()) if queue else print(-1)
    elif command == 'pop_back' :   print(queue.pop()) if queue else print(-1)
    elif command == 'size' :  print(len(queue))
    elif command == 'empty' : print(0) if queue else print(1)
    elif command == 'front' : print(queue[0]) if queue else print(-1)
    elif command == 'back' :  print(queue[-1]) if queue else print(-1)