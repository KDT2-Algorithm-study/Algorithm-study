import sys
input = sys.stdin.readline
a,b = map(int,input().split())
l = [[] for _ in range(a+1)]
check = [False]*(a+1)
for _ in range(b):
    x,y = map(int,input().split())
    l[x].append(y)
    l[y].append(x)

cnt = 0
def DFS(start):
    if check[start] == False :
      stack = [start]
      check[start] = True

      while stack:
        cur = stack.pop()
        for adj in l[cur]:
          if not check[adj]:
            check[adj] = True
            stack.append(adj)
      else:
        global cnt
        cnt += 1

for i in range(1,a+1):
    DFS(i)

print(cnt)