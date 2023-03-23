move = [(0,1), (1,0), (0,-1), (-1,0)]

for t in range(1,int(input())+1):
    n = int(input())
    snail = [[0] * n for _ in range(n)]
    x,y = 0,-1
    i = 1
    j = 0
    while i <= n*n:
        xa = x+move[j][0]
        yb = y+move[j][1]
        if xa < n and yb < n and snail[xa][yb] == 0:
            snail[xa][yb] = i
            i += 1
            x, y = xa, yb
        else:
            j = (j+1) % 4
    print(f'#{t}')
    for num in range(n):
        print(*snail[num])