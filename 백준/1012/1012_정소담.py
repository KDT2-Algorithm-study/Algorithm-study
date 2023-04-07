import sys
sys.setrecursionlimit(10**6)

direct = [(0,1),(1,0),(-1,0),(0,-1)]

def dfs(x,y):
    visit[x][y] = 1
    for d in direct:
        xd = x+d[0]
        yd = y+d[1]
        if 0 <= xd < n and 0 <= yd < m:
            if visit[xd][yd] == 0 and field[xd][yd] == 1:
                dfs(xd, yd)

for t in range(int(input())):
    m, n, cabbage = map(int,input().split())
    field = [[0]*m for _ in range(n)]
    visit = [[0]*m for _ in range(n)]
    cnt = 0
    for _ in range(cabbage):
        x,y = map(int,input().split())
        field[y][x] = 1
    for i in range(n):
        for j in range(m):
            if visit[i][j] == 0 and field[i][j] == 1:
                dfs(i,j)
                cnt += 1
    print(cnt)



# import sys
# sys.setrecursionlimit(10**6)
# 추가 안하면 런타임 에러 (RecursionError) 뜸 ㅠ....