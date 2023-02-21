import sys
from collections import deque

n = int(sys.stdin.readline())
result = deque()

for i in range(n):
    # 명령을 입력받는다
    command = sys.stdin.readline().split()
    try:
        # push
        # push_front: appendleft를 사용한다
        # push_back: append를 사용한다
        command[1] = int(command[1])
        if (command[0] == 'push_front'):
            result.appendleft(command[1])
        elif (command[0] == 'push_back'):
            result.append(command[1])
    except:
        # pop
        # pop_front: popleft를 사용한다
        # pop_back: pop을 사용한다
        if (command[0] == 'pop_front'):
            try:
                print(result.popleft())
            except:
                print(-1)
        elif (command[0] == 'pop_back'):
            try:
                print(result.pop())
            except:
                print(-1)
        # size: 덱의 길이를 출력한다
        elif (command[0] == 'size'):
            print(len(result))
        # empty: 덱이 비어있으면 1, 비어있지 않으면 0
        elif (command[0] == 'empty'):
            if len(result):
                print(0)
            else:
                print(1)
        # front: 인덱스가 0인 원소를 출력한다
        # 비어있는 경우 -1을 출력한다
        elif (command[0] == 'front'):
            try:
                print(result[0])
            except:
                print(-1)
        # back: 가장 뒤에 있는 원소를 출력한다
        # 비어있는 경우 -1을 출력한다
        elif (command[0] == 'back'):
            try:
                print(result[-1])
            except:
                print(-1)
