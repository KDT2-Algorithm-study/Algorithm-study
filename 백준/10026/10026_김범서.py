from collections import deque
import sys

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

# 적록색약이 아닌 사람이 봤을 때
def bfs(r, c):
    que = deque([[r, c]])

    while que:
        now = que.popleft()
        for i in range(4):
            nr = now[0] + dr[i]
            nc = now[1] + dc[i]
            if (0 <= nr < n) and (0 <= nc < n) and not visited_original[nr][nc]:
                if picture[now[0]][now[1]] == picture[nr][nc]:
                    visited_original[nr][nc] = True
                    que.append([nr, nc])


# 적록색약인 사람이 봤을 때
# RG와 B로 구분했다.
def cvd(r, c):
    que = deque([[r, c]])

    while que:
        now = que.popleft()
        for i in range(4):
            nr = now[0] + dr[i]
            nc = now[1] + dc[i]
            if (0 <= nr < n) and (0 <= nc < n) and not visited_cvd[nr][nc]:
                if (picture[now[0]][now[1]] in 'RG' and picture[nr][nc] in 'RG') or picture[now[0]][now[1]] == picture[nr][nc] == 'B':
                    visited_cvd[nr][nc] = True
                    que.append([nr, nc])


n = int(sys.stdin.readline())
visited_original = [[False for i in range(n)] for j in range(n)]
visited_cvd = [[False for i in range(n)] for j in range(n)]
picture = list()
original = 0
red_green = 0

# 그림 원본 데이터를 입력받는다
for i in range(n):
    picture.append(list(sys.stdin.readline().strip()))

# 구역 개수 세기
for i in range(n):
    for j in range(n):
        if not visited_original[i][j]:
            visited_original[i][j] = True
            bfs(i, j)
            original += 1
        if not visited_cvd[i][j]:
            visited_cvd[i][j] = True
            cvd(i, j)
            red_green += 1

print(original, red_green)


# CVD는 Color Vision Deficiency의 약자
