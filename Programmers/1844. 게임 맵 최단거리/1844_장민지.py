# 게임 맵 최단거리
from collections import deque
def solution(maps):
    N = len(maps)
    M = len(maps[0])
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    stack = deque([(0,0)])

    while stack:
        i, j = stack.popleft()

        for n in range(4):
            x = i + dx[n]
            y = j + dy[n]
            if 0 <= x < N and 0 <= y < M:
                if maps[x][y] == 1:
                    stack.append((x,y))
                    maps[x][y] = maps[i][j] + 1
    if maps[-1][-1] == 1:
        answer = -1
    else:
        answer = maps[-1][-1]
    return answer