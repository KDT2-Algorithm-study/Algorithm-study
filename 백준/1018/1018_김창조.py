# 1018. 체스판 다시 칠하기

import sys
from collections import deque

BOARD_SIZE = 8
chess_board = deque([
        "WBWBWBWB",
        "BWBWBWBW",
        "WBWBWBWB",
        "BWBWBWBW",
        "WBWBWBWB",
        "BWBWBWBW",
        "WBWBWBWB",
        "BWBWBWBW",
])

# input
n, m = map(int, sys.stdin.readline().rstrip().split())

# Read map
map_lst = []
for _ in range(n):
    map_lst.append(sys.stdin.readline().rstrip())

# solution
def get_correct_score(lst: list, pos: tuple) -> int:
    score = 0
    fix = 0
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            lst[pos[0] + i][pos[1] + j]
            # print(i, j)
            chess_board[i][j]
            if lst[pos[0] + i][pos[1] + j] == chess_board[i][j]:
                score += 1
            else:
                fix += 1

            # print(f"check if {lst[pos[0] + i][pos[1] + j] == chess_board[i][j]}")

    return (score, fix)

max_score = (0, 0)
for i in range(n - BOARD_SIZE + 1):
    for j in range(m - BOARD_SIZE + 1):
        score = 0
        pos = (i, j)

        score = get_correct_score(map_lst, pos)
        if score[0] > max_score[0]:
            max_score = score
            max_pos = pos

        chess_board.append(chess_board.popleft())

        score = get_correct_score(map_lst, pos)
        if score > max_score:
            max_score = score
            max_pos = pos

print(max_score[1])