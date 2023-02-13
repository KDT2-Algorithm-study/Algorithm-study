import sys

n = int(sys.stdin.readline())
stack = list()

for i in range(n):
    # 명령 읽기
    command = sys.stdin.readline().split()
    ## 리스트 'command'의 길이가 1일 때와 0일 때를 try-excpet문으로 구분했다.
    try:
        # push
        command[1] = int(command[1])
        if (command[0] == 'push'):
            stack.append(command[1])
    except:
        # pop
        if (command[0] == 'pop'):
            try:
                print(stack.pop())
            except:
                print(-1)
        # size
        elif (command[0] == 'size'):
            print(len(stack))
        # empty
        elif (command[0] == 'empty'):
            if len(stack):
                print(0)
            else:
                print(1)
        # top
        elif (command[0] == 'top'):
            try:
                print(stack[-1])
            except:
                print(-1)
