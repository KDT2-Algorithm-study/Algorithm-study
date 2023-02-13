import sys
input = sys.stdin.readline
list1 = []

N = int(input())
for n in range(N) :
    commend = input().strip()
    # print(list1 ,'before')

    if commend[:4] == 'push' :
        list1.append(int(commend[5:]))

    elif commend == 'pop' :
        if list1 : print(list1.pop())
        else : print(-1)

    elif commend == 'size' :
        print(len(list1))

    elif commend == 'empty' :
        if list1 : print(0)
        else : print(1)

    elif commend == 'top' :
        if list1 : print(list1[-1])
        else : print(-1)

    # print(list1 ,'after')