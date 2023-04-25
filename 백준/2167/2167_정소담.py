import sys
input = sys.stdin.readline

n,m = map(int,input().split())
num = [list(map(int,input().split())) for _ in range(n)]
cnt = [[0 for _ in range(m+1)] for _ in range(n+1)]

for x in range(1,n+1):
    for y in range(1,m+1):
        cnt[x][y] = num[x-1][y-1] + cnt[x-1][y] + cnt[x][y-1] - cnt[x-1][y-1]

for _ in range(int(input())):
    x,y,i,j = map(int,input().split())
    print(cnt[i][j]-cnt[i][y-1]-cnt[x-1][j]+cnt[x-1][y-1])