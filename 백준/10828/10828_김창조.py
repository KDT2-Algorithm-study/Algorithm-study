# 10828

import sys

cmd_lst = ["push", "pop", "size", "empty", "top"]
stack = []

for _ in range(int(sys.stdin.readline().strip())):
    cmd = sys.stdin.readline().strip()
    
    if cmd_lst[0] in cmd:
        num = int(cmd.split()[1])
        stack. append(num)
        
    elif cmd_lst[1] in cmd:
        if stack:
            print(stack.pop())
        else:
            print(-1)
        
    elif cmd_lst[2] in cmd:
        print(len(stack))
        
    elif cmd_lst[3] in cmd:
        if stack:
            print(0)
        else:
            print(1)
        
    elif cmd_lst[4] in cmd:
        if stack:
            print(stack[-1])
        else:
            print(-1)
        
    else:
        sys.exit("Wrong Input")