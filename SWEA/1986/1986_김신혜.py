import sys
sys.stdin = open("input.txt","r")

T = int(input())
for t in range(1, T+1):
    N = int(input())
    num = 0
    for n in range(1, N+1):
        if n%2 != 0:
            num += n
        else:
            num -= n
    print(f'#{t} {num}')