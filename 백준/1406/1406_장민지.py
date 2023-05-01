import sys

string = list(sys.stdin.readline().rstrip())
string2 = []
for _ in range(int(sys.stdin.readline())):
    order = list(sys.stdin.readline().split())
    if order[0] == 'L':
        if string:
            string2.append(string.pop())

    elif order[0] == 'D':
        if string2:
            string.append(string2.pop())

    elif order[0] == 'B':
        if string:
            string.pop()
    else:
        
        string.append(order[1])
string.extend(reversed(string2))
print(''.join(string))