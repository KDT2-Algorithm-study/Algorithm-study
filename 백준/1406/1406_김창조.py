# 1406. 에디터

import sys
from collections import deque
input = sys.stdin.readline

front_word = deque(list(input().rstrip()))
back_word = deque()

M = int(input())

for _ in range(M):
    cmd = input().rstrip()
    
    if 'L' == cmd:
        if front_word:
            back_word.appendleft(front_word.pop())
    elif 'D' == cmd:
        if back_word:
            front_word.append(back_word.popleft())
    elif 'B' == cmd:
        if front_word:
            front_word.pop()
    elif 'P' in cmd:
        front_word.append(cmd[2])
        
print(''.join(front_word)+''.join(back_word))