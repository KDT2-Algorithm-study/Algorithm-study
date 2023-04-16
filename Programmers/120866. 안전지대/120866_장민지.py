def solution(board):
    dx = [-1, 1, 0, 0, 1, 1, -1, -1]
    dy = [0, 0, -1, 1, 1, -1, 1, -1]
    n = len(board)
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                
                for k in range(8):
                    x = i + dx[k]
                    y = j + dy[k]
                    if 0 <= x < n and 0 <= y < n:
                        if board[x][y] == 1:
                            continue
                        board[x][y] = 2
    answer = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                answer += 1
    return answer