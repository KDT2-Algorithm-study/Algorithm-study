import sys
sys.setrecursionlimit(10000)

direct = [(0,1),(1,0),(-1,0),(0,-1)]
def dfs(y, x):
    visit[y][x] = 1

    for d in direct:
        yd = y+d[0]
        xd = x+d[1]
        
        # yd가 0이면 맨 윗줄 / 세로 높이는 0 ~ h-1 
        # xd가 0이면 맨 왼쪽 줄 / 가로 넓이는 0 ~ w-1
        if 0 <= yd < h and 0 <= xd < w: 
            
            # 방문을 안 했는데(0) 배추가 있는 경우(1) 
            if visit[yd][xd] == 0 and field[yd][xd] == 1:
                dfs(yd, xd)

for t in range(int(input())):
    w, h, k = map(int,input().split())
    field = [[0]*w for _ in range(h)]
    visit = [[0]*w for _ in range(h)]
    cnt = 0
    for _ in range(k):
        x, y = map(int,input().split())
        field[y][x] = 1
    for y in range(h):
        for x in range(w):
            # 방문을 안 했는데(0) 배추가 있는 경우(1) 
            if visit[y][x] == 0 and field[y][x] == 1:
                dfs(y, x)
                cnt += 1
    print(cnt)


