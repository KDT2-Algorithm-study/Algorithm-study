import sys
stack = []
for _ in range(int(input())):
    command = sys.stdin.readline().split()
    if "push" in command:
        stack.append(command[1])
    elif "pop" in command:
        print(stack.pop()) if stack else print(-1)
    elif "size" in command:
        print(len(stack))
    elif "empty" in command:
        print(0) if stack else print(1)
    elif "top" in command:
        print(stack[-1]) if stack else print(-1)
