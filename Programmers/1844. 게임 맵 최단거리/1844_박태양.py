from collections import deque

def solution(maps):
    d = [(1,0),(-1,0),(0,1),(0,-1)]
    n = len(maps[0])
    m = len(maps)
    q = deque()
    q.append((0,0))

    while q:
        x, y = q.popleft()
        for dx, dy in d:
            mx = x + dx
            my = y + dy
            if 0<=mx<n and 0<=my<m:
                if maps[my][mx] == 1:
                    q.append((mx,my))
                    maps[my][mx] = maps[y][x] + 1


    if maps[-1][-1] == 1:
        answer = -1
    else:
        answer = maps[-1][-1]
    return answer

m = [[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 0], [0, 0, 0, 0, 1]]
print(solution(m))

