from collections import deque
def solution(maps):
    answer = 0
    direct = [(1,0), (0,1), (-1,0), (0,-1)]
    queue = deque()
    n = len(maps)
    m = len(maps[0])
    def bfs(x,y):
        queue.append((x,y))
        while queue:
            x, y = queue.popleft()
            for d in direct:
                xd, yd = x + d[0], y + d[1]
                if 0 <= xd < n and 0 <= yd < m and maps[xd][yd] == 1:
                        maps[xd][yd] = maps[x][y] + 1
                        queue.append((xd,yd))
        if maps[-1][-1] == 1:
            return -1
        return maps[-1][-1]
    answer = bfs(0,0)
    return answer