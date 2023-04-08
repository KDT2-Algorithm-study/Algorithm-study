for _ in range(int(input())):
    d = [(1,0),(-1,0),(0,1),(0,-1)]
    def dfs(x,y):
        global cnt
        graph[y][x] = 0
        stack = []
        stack.append((x,y))

        while stack:
            kx,ky = stack.pop()
            for dx,dy in d:
                mx = kx+dx
                my = ky+dy
                if 0<=mx<m and 0<=my<n and graph[my][mx] == 1:
                    graph[my][mx] = 0
                    stack.append((mx,my))
        
        else:
            cnt +=1
                


    m,n,k = map(int,input().split())
    graph = [[0]*m for _ in range(n)]
    for _ in range(k):
        a,b = map(int,input().split())
        graph[b][a] = 1

    cnt = 0
    for i in range(m):
        for j in range(n):
            if graph[j][i] == 1:
                dfs(i,j)
    print(cnt)