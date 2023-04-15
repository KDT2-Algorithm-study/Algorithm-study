import sys
input = sys.stdin.readline    

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]

hacking_num = [0 for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    graph[b].append(a)

stack = []
for i in range(1,n+1):
    cnt = 0
    check = set()
    stack.append(i)
    check.add(i)

    while stack:
        k = stack.pop()
        hacking_num[i] +=1
        for j in graph[k]:
            if  j not in check:
                stack.append(j)
                check.add(j)
                
max_hacking_num = max(hacking_num)
for i in range(1,n+1):
    if max_hacking_num == hacking_num[i]:
        print(i,end=' ')