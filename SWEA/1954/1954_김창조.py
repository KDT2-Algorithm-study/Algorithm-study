# 1954. 달팽이 숫자

from collections import deque

test_case = int(input())
for tc in range(1, test_case+1):
    n = int(input())
    
    lst = [[0] * n for _ in range(n)]
    delta = deque([(0, 1), (1, 0), (0, -1), (-1, 0)])
    cnt, i, j = 1, 0, 0
    dx, dy = delta[0]
    
    while cnt <= n * n:
        lst[i][j] = cnt
        nx = i + dx
        ny = j + dy
        if (nx) >= n or (nx) < 0 or (ny) >= n or (ny) < 0 or lst[nx][ny]:
            delta.rotate(-1)
            dx, dy = delta[0]
        i += dx
        j += dy
        cnt += 1
        
    print(f'#{tc}')
    for i in range(n):
        print(' '.join(map(str, lst[i])))