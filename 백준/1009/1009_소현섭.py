import sys

T = int(sys.stdin.readline().rstrip())
for i in range(T):
    a, b = map(int, sys.stdin.readline().split())
    b = b%4
    if b%4 ==0 :
        b = 4
    s = a**b
    if s%10 == 0:
        print(10)
    else:
        print(s%10)