import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

def dfs(n):
    visit.append(n)
    for i in line[n]:
        if i not in visit:
            dfs(i)


n, m = map(int,input().split())
line = [[] for _ in range(n+1)]
visit = []
cnt = 0

for _ in range(m):
    x,y = map(int,input().split())
    line[x].append(y)
    line[y].append(x)

for i in range(1,n+1):
    if i not in visit:
        dfs(i)
        cnt += 1
print(cnt)