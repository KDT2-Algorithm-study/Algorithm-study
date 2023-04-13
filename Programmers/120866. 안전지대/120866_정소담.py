direct = [(1,0),(1,1),(0,1),(-1,0),(-1,-1),(0,-1),(-1,1),(1,-1)]
def solution(board):
    answer = 0
    n = len(board)
    visit = [[0]*n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if board[x][y] == 1 and visit[x][y] == 0:
                visit[x][y] = 1
                for d in direct:
                    xd, yd = x + d[0], y + d[1]
                    if 0 <= xd < n and 0 <= yd < n and board[xd][yd] == 0:
                        board[xd][yd] = 1
                        visit[xd][yd] = 1
    for i in board:
        answer += i.count(0)
    return answer