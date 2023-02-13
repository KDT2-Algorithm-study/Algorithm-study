import sys
input = sys.stdin.readline

stack = []
for _ in range(int(input())):
    x = input().rstrip('\n')
    n = x[:5]
    if n == 'push ':
        stack.append(int(x[5:]))
    elif x == 'pop':
        if len(stack) > 0:
            print(stack.pop())
        else:
            print(-1)
    elif x == 'size':
        print(len(stack))
    elif x == 'empty':
        if len(stack) > 0:
            print(0)
        else:
            print(1)
    elif x == 'top':
        if len(stack) > 0:
            print(stack[-1])
        else:
            print(-1)