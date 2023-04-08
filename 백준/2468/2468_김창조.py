# 2468. 안전 영역

import sys
from collections import deque
# sys.setrecursionlimit(10 ** 4)    # recursion option

delta = [
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1)
]

def check_valid(pos: tuple, n: int):
    global area_temp
    
    if 0 <= pos[0] < n and 0 <= pos[1] < n :
        if area_temp[pos[0]][pos[1]] > 0:
            return True
    return False

def dfs_recursion(pos: tuple):
    global delta, area_temp
    
    for dy, dx in delta:
        new_pos = (pos[0]+dy, pos[1]+dx)
        if check_valid(new_pos, n):
            area_temp[new_pos[0]][new_pos[1]] = 0
            dfs_recursion(new_pos)

def bfs_recursion(pos: tuple):
    global delta, area_temp
    
    lst = list()
    for dy, dx in delta:
        new_pos = (pos[0]+dy, pos[1]+dx)
        if check_valid(new_pos, n):
            area_temp[new_pos[0]][new_pos[1]] = 0
            lst.append(new_pos)
    
    for pos_ in lst:
        bfs_recursion(pos_)

def dfs_loop(position: tuple):
    global delta, area_temp
    stack = [position]
    
    while stack:
        pos = stack.pop()

        for dy, dx in delta:
            new_pos = (pos[0]+dy, pos[1]+dx)
            if check_valid(new_pos, n):
                area_temp[new_pos[0]][new_pos[1]] = 0
                stack.append(new_pos)

def bfs_loop(position: tuple):
    global delta, area_temp
    deq = deque([position])
    
    while deq:
        pos = deq.popleft()

        for dy, dx in delta:
            new_pos = (pos[0]+dy, pos[1]+dx)
            if check_valid(new_pos, n):
                area_temp[new_pos[0]][new_pos[1]] = 0
                deq.append(new_pos)
    

n = int(input())
area = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
heights = set(sum(area, []))

answer = 1
for height in heights:
    cnt = 0
    area_temp = [[i - height for i in line] for line in area]
    for i in range(n):
        for j in range(n):
            if area_temp[i][j] <= 0:
                continue
            cnt += 1
            
            area_temp[i][j] = 0
            # dfs_recursion((i, j))
            # bfs_recursion((i, j))
            # dfs_loop((i, j))
            bfs_loop((i, j))
            
    answer = cnt if cnt > answer else answer
    
print(answer)