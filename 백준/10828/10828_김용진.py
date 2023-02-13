# 스택

import sys
sys.stdin = open('input.txt','r')

T = int(input())
Stack =[]
for t in range(T):
    word = []
    word = list(map(str,sys.stdin.readline().split()))
    if word[0] == 'push':
        Stack.append(int(word[1]))
    elif word[0] == 'pop':
        if len(Stack) == 0:
            print(-1)
        else:
            print(Stack.pop())            
    elif word[0] == 'size':
        print(len(Stack))
    elif word[0] == 'empty':
        if len(Stack) == 0:
            print(1)
        else:
            print(0)
    elif word[0] == 'top':
        if len(Stack) == 0:
            print(-1)
        else:
            print(Stack[-1])