import sys
sys.stdin = open('test.txt', 'r')

T = int(input())
for t in range(T):
    N = int(input())
    number = 10000

    print(f'#{t+1}')
    for i in range(4):
        for i in [5, 1]:
            print(N // (number * i), end=' ')
            N %= (number * i)
        number //= 10

    print()
