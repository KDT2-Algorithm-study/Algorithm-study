from collections import deque
import sys
input = sys.stdin.readline
tc = int(input())
l = deque()
for i in range(tc):
    a = input().rstrip()
    if a == 'pop_front':
        try:
            print(l.popleft())
        except:
            print('-1')
            continue
    elif a == 'pop_back':
        try:
            print(l.pop())
        except:
            print('-1')
            continue
    elif a == 'size':
        print(len(l))
    elif a == 'empty':
        if len(l)==0:
            print('1')
        else:
            print('0')
    elif a == 'front':
        if l:
            print(l[0])
        else:
            print('-1')
    elif a == 'back':
        if l:
            print(l[-1])
        else:
            print('-1')
    else:
        b,c = a.split()
        if b == 'push_front':
            l.appendleft(c)
        else:
            l.append(c)
