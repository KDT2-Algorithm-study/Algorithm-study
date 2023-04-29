# 에디터

import sys
sys.stdin = open('input.txt','r')

word = list(input())
a = []
T = int(input())

for _ in range(T):
    editor = list(map(str,input().split()))
    if len(editor) == 2:
        word.append(editor[1])
    else:
        if editor[0] == 'L':
            if len(word) != 0:
                a.append(word.pop())
            else:
                pass 
        elif editor[0] == 'B':
            if len(word) != 0:
                word.pop()
            else:
                pass
        elif editor[0] == 'D':
            if len(a) != 0:
                word.append(a.pop())
            else:
                pass

for _ in range(len(a)):
    word.append(a.pop())

print(''.join(word))


