# 10026. 적록색약

import sys
from collections import deque
from pprint import pprint
sys.setrecursionlimit(10 ** 6)

answer = [0, 0]
DELTA = [(0, 1), (0, -1), (1, 0), (-1, 0)]

n = int(input())
area = list()
area2= list()

for _ in range(n):
    line = list(sys.stdin.readline().rstrip())
    area.append(line)
    area2.append([char if char != 'G' else 'R' for char in line])
    
# pprint(area)
# pprint(area2)

def check_valid(pos: tuple, n: int):
    if 0 <= pos[0] < n and 0 <= pos[1] < n:
        return True
    return False

def bfs(lst: list, start: tuple):
    deq = deque([start])
    
    color = lst[start[0]][start[1]]
    lst[start[0]][start[1]] = 0
    
    while deq:
        pos = deq.popleft()
        for dy, dx in DELTA:
            new_pos = (pos[0]+dy, pos[1]+dx)
            if not check_valid(new_pos, n):
                continue
            if color == lst[new_pos[0]][new_pos[1]]:
                deq.append(new_pos)
                lst[new_pos[0]][new_pos[1]] = 0

for i in range(n):
    for j in range(n):
        if not area[i][j]:
            continue
        
        answer[0] += 1
        bfs(area, (i, j))
        
# 적록색약이 본 경우
for i in range(n):
    for j in range(n):
        if not area2[i][j]:
            continue
        
        answer[1] += 1
        bfs(area2, (i, j))

print(*answer)