import sys

stack = []
for _ in range(int(sys.stdin.readline())):
    command = sys.stdin.readline().strip()
    if 'push' in command:
        stack.append(command.split()[1])
    elif command == 'top':
        print(stack[-1]) if stack else print(-1)
    elif command == 'size':
        print(len(stack))
    elif command == 'empty':
        print(1) if not stack else print(0)
    elif command == 'pop':
        print(stack.pop()) if stack else print(-1)