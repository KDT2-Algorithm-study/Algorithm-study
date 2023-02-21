'''10866번 덱
문제
정수를 저장하는 덱(Deque)를 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.


입력
첫째 줄에 주어지는 명령의 수 N (1 ≤ N ≤ 10,000)이 주어진다. 
둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다. 주어지는 정수는 1보다 크거나 같고, 100,000보다 작거나 같다.

출력
출력해야하는 명령이 주어질 때마다, 한 줄에 하나씩 출력한다.'''

import sys
from collections import deque
sys.stdin = open("input.txt", "r")

N = int(sys.stdin.readline())
Q = deque()
for n in range(N):
    command = sys.stdin.readline().split()  # 명령을 입력받는다
    cmd = command[0]

    if cmd[0:4] == 'push':
        if cmd[-1] == 't':          # push_front X  정수 X를 덱의 앞에 넣는다.
            Q.appendleft(int(command[1]))
        elif cmd[-1] == 'k':        # push_back X   정수 X를 덱의 뒤에 넣는다.
            Q.append(int(command[1]))

    elif cmd[0:3] == 'pop':
        if len(Q) != 0:
            if cmd[-1] == 't':      # pop_front     덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 
                print(Q.popleft())
            elif cmd[-1] == 'k':    # pop_back      덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다.
                print(Q.pop())
        else:
            print(-1)               # 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.

    elif cmd == 'size':             # size          덱에 들어있는 정수의 개수를 출력한다.
        print(len(Q))

    elif cmd == 'empty':            # empty         덱이 비어있으면 1을, 아니면 0을 출력한다.
        if len(Q) != 0:
            print(0)
        else:
            print(1)
            
    elif cmd == 'front':            # front         덱의 가장 앞에 있는 정수를 출력한다.
        if len(Q) != 0:
            print(Q[0])
        else:
            print(-1)               # 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.

    elif cmd == 'back':            # back           덱의 가장 뒤에 있는 정수를 출력한다.
        if len(Q) != 0:
            print(Q[-1])
        else:
            print(-1)               # 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.

# push_back 1
# push_front 2
# front
# back
# size
# empty
# pop_front
# pop_back
# pop_front
# size
# empty
# pop_back
# push_front 3
# empty
# front

# 2
# 1
# 2
# 0
# 2
# 1
# -1
# 0
# 1
# -1
# 0
# 3
