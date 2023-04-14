# 120866. 안전지대

def solution(board):
    answer = 0
    size = len(board)
    
    DELTA = [
        (0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)
    ]
    
    for i in range(size):
        for j in range(size):
            if board[i][j] != 1:
                continue
            
            for dy, dx in DELTA:
                pos = (i+dy, j+dx)
                if not check_valid(pos, size):
                    continue
                if not board[pos[0]][pos[1]]:
                    board[pos[0]][pos[1]] = 2
    
    answer = sum([line.count(0) for line in board])
    return answer


def check_valid(pos: tuple, size: int):
    if 0 <= pos[0] < size and 0 <= pos[1] < size:
        return True
    return False