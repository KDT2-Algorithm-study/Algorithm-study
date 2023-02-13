import sys

def stack_check(s):
    if s == 'pop':
        if len(stack) == 0:
            return -1
        else:
            return stack.pop()

    elif s == 'top':
        if len(stack) == 0:
            return -1
        else:
            return stack[-1]

stack = []
N = int(sys.stdin.readline().rstrip())
for _ in range(N):
    command = sys.stdin.readline().rstrip()

    if command[0:4] == 'push':
        stack.append(int(command[5:]))

    elif command == 'pop':
        print(stack_check('pop'))

    elif command == 'size':
        print(len(stack))
    
    elif command == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)    

    elif command == 'top':
        print(stack_check('top'))