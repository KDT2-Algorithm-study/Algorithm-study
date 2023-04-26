import sys

stk1 = list(sys.stdin.readline().strip())
stk2 = []

n = int(input())

for line in sys.stdin:
    if line[0] == 'L':
        if stk1: stk2.append(stk1.pop())
        else: continue

    elif line[0] == 'D':
        if stk2: stk1.append(stk2.pop())
        else: continue

    elif line[0] == 'B':
        if stk1: stk1.pop()
        else: continue

    elif line[0] == 'P':
        stk1.append(line[2])

print(''.join(stk1 + list(reversed(stk2))))