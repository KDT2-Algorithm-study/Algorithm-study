def solution(board):
    answer = 0
    for x in range(len(board)):
        board[x].insert(0, 2)
        board[x].append(2)
    board.insert(0, [2 for x in range(len(board)+2)])
    board.append([2 for x in range(len(board)+2)])
    for x in range(1, len(board)-1):
        for y in range(1, len(board[0])-1):
            if board[x][y] == 1:
                if board[x-1][y-1] == 0:
                    board[x-1][y-1] = 2
                if board[x-1][y] == 0:
                    board[x-1][y] = 2
                if board[x-1][y+1] == 0:
                    board[x-1][y+1] = 2
                if board[x][y-1] == 0:
                    board[x][y-1] = 2
                if board[x][y+1] == 0:
                    board[x][y+1] = 2
                if board[x+1][y-1] == 0:
                    board[x+1][y-1] = 2
                if board[x+1][y] == 0:
                    board[x+1][y] = 2
                if board[x+1][y+1] == 0:
                    board[x+1][y+1] = 2
    for x in board:
        answer += x.count(0)
    return answer