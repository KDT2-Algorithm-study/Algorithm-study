# 덱

import sys
sys.stdin = open('input.txt','r')
from collections import deque

a = deque()
T = int(input())

for t in range(T):
    word = list(map(str,sys.stdin.readline().split()))
    if word[0] == 'push_front':
        a.appendleft(word[1])
    elif word[0] == 'push_back' :
        a.append(word[1])
    elif word[0] == 'pop_front':
        if not a:
            print(-1)
        else:
            print(a.popleft())        
    elif word[0] == 'pop_back':
        if not a:
            print(-1)
        else:
            print(a.pop())
    elif word[0] == 'size':
        print(len(a))
    elif word[0] == 'empty':
        if not a:
            print(1)
        else:
            print(0)
    elif word[0] == 'front':
        if not a:
            print(-1)
        else:
            print(a[0])
    elif word[0] == 'back':
        if not a:
            print(-1)
        else:
            print(a[-1])