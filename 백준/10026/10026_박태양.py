import copy
n = int(input())
graph = []
for i in range(n):
    graph.append(list(input()))

graphd = copy.deepcopy(graph)
d = [(0,1),(0,-1),(1,0),(-1,0)]

def dfs(x,y):
    global mf
    stack = [(x,y)]
    color = graph[y][x]
    graph[y][x] = '0'
    while stack:
        x1,y1 = stack.pop()
        for dx,dy in d:
            mx = x1+dx
            my = y1+dy
            if 0<=mx<n and 0<=my<n:
                if graph[my][mx] == color:
                    graph[my][mx] = '0'
                    stack.append((mx,my))

def dfsGR(x,y):
    global mf
    stack = [(x,y)]
    color = graphd[y][x]
    graphd[y][x] = '0'
    while stack:
        x1,y1 = stack.pop()
        for dx,dy in d:
            mx = x1+dx
            my = y1+dy
            if color == 'B':
                if 0<=mx<n and 0<=my<n:
                    if graphd[my][mx] == color:
                        graphd[my][mx] = '0'
                        stack.append((mx,my))
            else:
                if 0<=mx<n and 0<=my<n:
                    if graphd[my][mx] in ['G','R']:
                        graphd[my][mx] = '0'
                        stack.append((mx,my))



cnt1 = 0
cnt2 = 0
for i in range(n):
    for j in range(n):
        if graph[i][j] != '0':
            dfs(j,i)
            cnt1 += 1
        if graphd[i][j] != '0':
            dfsGR(j,i)
            cnt2 += 1


print(cnt1,cnt2)
