import sys
# sys.stdin = open("input.txt", "r")
T = int(sys.stdin.readline())
for t in range(T):
    H, W ,N = map(int,sys.stdin.readline().split())
    y = (N//H) + 1
    x = N % H
    # 만약 나머지가 0이 나오면 위치는 가장 윗층이 되므로 H / y도 한칸 왼쪽으로 당겨진다.
    if x == 0 :
        x = H
        y -= 1
    print(x*100 +y)
