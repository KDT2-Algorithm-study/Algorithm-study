n = int(input())
lst = list()
for _ in range(n):
    command = input().split()
    if command[0] == 'push':
        lst.append(command[1])
    elif command[0] == 'pop':
        if lst:
            print(lst.pop())
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(lst))
    elif command[0] == 'empty':
        if lst:
            print(0)
        else:
            print(1)
    elif command[0] == 'top':
        if lst:
            print(lst[-1])
        else:
            print(-1)      