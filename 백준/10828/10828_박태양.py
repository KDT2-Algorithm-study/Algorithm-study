import sys
input = sys.stdin.readline
a = int(input())
l = []
for i in range(a):
    b = input().rstrip()
    if b[:4] == 'push':
        t,num = b.split()
        l.append(int(num))
    elif b == 'top' :
        if len(l) !=0:
            print(l[-1])
        else:
            print('-1')
    elif b == 'size':
        print(len(l))
    elif b == 'empty':
        if len(l) ==0:
            print('1')
        else : 
            print('0')
    elif b == 'pop':
        if len(l) ==0:
            print('-1')
        else:
            print(l.pop())