N = int(input())
graph = []
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
result = []

for _ in range(N):
    graph.append(list(map(int, input().split())))

# 최고 높이까지만 진행하기 위해 max 구하기
max_height = max(map(max, graph))
for height in range(0, max_height):
    stack = []
    safety = [[False]*N for _ in range(N)]
    

    # 높이에 따른 safty 만들기 (높이 이상이면 안전하므로 True)
    for i in range(N):
        for j in range(N):
            if graph[i][j] > height:
                safety[i][j] = True
            
    # print(safety)
    cnt = 0
    # safty 리스트 돌기
    for x in range(N):
        for y in range(N):
            # 안전한 높이이면 사방으로 돌기
            if safety[x][y] == True:
                stack.append((x,y))
                cnt += 1
            while stack:
                a, b = stack.pop()
                for z in range(4):
                    mx = a + dx[z]
                    my = b + dy[z]
                    if 0 <= mx < N and 0 <= my < N:
                        if safety[mx][my] == True:
                            safety[mx][my] = False
                            stack.append((mx, my))

    result.append(cnt)
print(max(result))