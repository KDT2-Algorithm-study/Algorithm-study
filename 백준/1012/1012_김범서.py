from collections import deque
import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    m, n, k = map(int, input().split())
    farm = [[0 for j in range(m)] for l in range(n)]
    result = 0
    que = deque()

    for j in range(k):
        x, y = map(int, input().split())
        farm[y][x] = 1

    for j in range(n):
        for l in range(m):
            if farm[j][l] == 1:
                que.append((j, l))
                farm[j][l] = 2
                while que:
                    r, c = que.popleft()
                    for dr, dc in ([1, 0], [0, 1], [-1, 0], [0, -1]):
                        nr, nc = r + dr, c + dc
                        if (0 <= nr < n) and (0 <= nc < m) and farm[nr][nc] == 1:
                            farm[nr][nc] = 2
                            que.append((nr, nc))
                result += 1
    
    print(result)
