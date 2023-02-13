import sys

T = int(sys.stdin.readline())

stack = []

for i in range(T):
    function = sys.stdin.readline().split()
    order = function[0]

    if order == 'push':
        stack.append(function[1]) # int

    elif order == 'pop':
        if stack == []:
            print(-1)
        else:
            print(stack.pop())
            
    elif order == 'size':
        print(len(stack))
    
    elif order == 'empty':
        if stack == []:
            print(1)
        else:
            print(0)

    elif order == 'top':
        if stack == []:
            print(-1)
        else:
            print(stack[-1])