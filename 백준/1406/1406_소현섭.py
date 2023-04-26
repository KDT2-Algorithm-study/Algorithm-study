import sys

stack_l = list(input())
stack_r = []
for _ in range(int(input())):
    cmd = sys.stdin.readline().split()

    if cmd[0] == "L" and stack_l:
        stack_r.append(stack_l.pop())
    elif cmd[0] == "D" and stack_r:
        stack_l.append(stack_r.pop())
    elif cmd[0] == "B" and stack_l:
        stack_l.pop()
    elif cmd[0] == "P":
        stack_l.append(cmd[1])
print("".join(stack_l + list(reversed(stack_r))))