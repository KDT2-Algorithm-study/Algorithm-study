# 1844. 게임 맵 최단거리

from collections import deque

DELTA = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def solution(maps):
    answer = 0
    size = (len(maps), len(maps[0]))
    deq = deque([(0,0)])
    
    while deq:
        pos = deq.popleft()
        for dy, dx in DELTA:
            new_pos = (pos[0]+dy, pos[1]+dx)
            if not check_valid(new_pos, size):
                continue
            if maps[new_pos[0]][new_pos[1]] == 1:
                deq.append(new_pos)
                maps[new_pos[0]][new_pos[1]] = maps[pos[0]][pos[1]] + 1
    
    answer = maps[size[0] - 1][size[1] - 1]
    if answer == 1:
        answer = -1
    return answer


def check_valid(new_pos:tuple, size: tuple):
    if 0 <= new_pos[0] < size[0] and 0 <= new_pos[1] < size[1]:
        return True
    return False

"""
import copy

def solution2(maps):
    answer = 0
    
    START = (0, 0)
    answer = dfs(maps, START)
    
    return answer
    
    
def dfs(maps: list, pos: tuple):
    # print(f'{pos} : {maps[pos[0]][pos[1]]}')
    size = (len(maps), len(maps[0]))
    if pos[0] == size[0]-1 and pos[1] == size[1]-1:
        return 1
    
    delta = [
        (1, 0), (-1, 0), (0, 1), (-1, 0)
    ]
    
    maps[pos[0]][pos[1]] = 0
    result = list()
    for dy, dx in delta:            
        new_pos = (pos[0]+dy, pos[1]+dx)
        if not check_valid(new_pos, size):
            continue
            
        if maps[new_pos[0]][new_pos[1]]:
            q.append(new_pos)
    
    for new_pos in q:
        temp = dfs(copy.deepcopy(maps), new_pos) + 1
        if temp > 0:
            result.append(temp)
            
    if result:
        return min(result)
    else:
        return -1
"""
            
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
print(solution([[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]]))
# print(solution([[1,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,1]]))
# print(solution([[1,1,1,1,1],[0,0,0,0,1],[0,0,0,0,1],[0,0,0,0,1],[0,0,0,0,1]]))
# print(solution([[1,1,1,1,1],[0,0,0,0,1],[0,0,0,0,1],[0,0,0,0,1]]))
# print(solution([[1],[1],[1],[1]]))
# print(solution([[1],[0],[0],[1]]))
# print(solution([[1,1],[1,1],[1,0],[0,1]]))