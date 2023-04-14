def solution(board):
    N = len(board)
    dx = [-1, 1, 0, 0, -1, -1, 1, 1]
    dy = [0, 0, -1, 1, -1, 1, -1, 1]
    
    li = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                li.append((i,j))
                    
    for x, y in li:
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                board[nx][ny] = 1

    cnt = 0
    for x in range(N):
        for y in range(N):
            if board[x][y] == 0:
                cnt += 1
    return cnt