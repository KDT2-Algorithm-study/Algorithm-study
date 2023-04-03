import sys
N = int(sys.stdin.readline())
cnt = 0
while True:
    if N%5 == 0:
        print(cnt + N//5)
        break
    N -= 3
    cnt += 1
    if N < 0:
        print(-1)
        break