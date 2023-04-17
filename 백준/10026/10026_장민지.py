N = int(input())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

graph = []
for _ in range(N):
    string = input()
    lst = []
    for s in string:
        lst.append(s)
    graph.append(lst)

visited = [[False]*N for _ in range(N)]

stack = []
cnt = 0
for i in range(N):
    for j in range(N):
        if visited[i][j] == False:
            stack.append((i,j))
            while stack:
                cur = stack.pop()
                colour = graph[cur[0]][cur[1]]
                for n in range(4):
                    x = cur[0] + dx[n]
                    y = cur[1] + dy[n]
                    if 0 <= x < N and 0 <= y < N:
                        if graph[x][y] == colour and visited[x][y] == False:
                            visited[x][y] = True
                            stack.append((x,y))
            cnt += 1

visited = [[False]*N for _ in range(N)]

stack = []
cnt2 = 0
for i in range(N):
    for j in range(N):
        if visited[i][j] == False:
            # R, G인 경우
            if graph[i][j] == "R" or graph[i][j] == "G":
                stack.append((i,j))
                while stack:
                    cur = stack.pop()
                    for n in range(4):
                        x = cur[0] + dx[n]
                        y = cur[1] + dy[n]
                        if 0 <= x < N and 0 <= y < N:
                            if graph[x][y] == "R" or graph[x][y] == "G":
                                if visited[x][y] == False:
                                    visited[x][y] = True
                                    stack.append((x,y))
                cnt2 += 1
            else:
                stack.append((i,j))
                while stack:
                    cur = stack.pop()
                    colour = graph[cur[0]][cur[1]]
                    for n in range(4):
                        x = cur[0] + dx[n]
                        y = cur[1] + dy[n]
                        if 0 <= x < N and 0 <= y < N:
                            if graph[x][y] == colour and visited[x][y] == False:
                                visited[x][y] = True
                                stack.append((x,y))
                cnt2 += 1

print(cnt, cnt2)