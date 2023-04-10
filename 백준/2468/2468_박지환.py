n = int(input())
map_list = [list(map(int, input().split())) for _ in range(n)]
res = [] # 높이별 안전한 영역의 개수를 담을 통

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]


m = 0
for c in range(n): # 최댓값 뽑아내기
    for r in range(n):
        if m < map_list[c][r]:
            m = map_list[c][r]

for water in range(m): # 물 높이 낮을 때부터
    cnt = 0 # 높이별 안전한 영역의 개수
    visited = [[0]*n for _ in range(n)] 
    for a in range(n):
        for b in range(n):
            if map_list[a][b] > water:
                visited[a][b] = 1

for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            visited[i][j] = 1
            stack = []
            stack.append(j)
            stack.append(i)
            cnt += 1
            
            while stack:
                y = stack.pop()
                x = stack.pop()
                
                for k in range(4):
                    ny = y + dy[k]
                    nx = x + dx[k]
                if  0 <= nx < n and 0 <= ny < n:
                    if visited[ny][nx] == 1:
                        visited[ny][nx] = 0
                        stack.append(nx)
                        stack.append(ny)
            
    res.append(cnt)
    
print(max(res))