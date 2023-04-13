# 안전지대

def solution(board):
    N = len(board)
    dx =[0,0,1,-1,1,1,-1,-1]
    dy =[-1,1,0,0,1,-1,1,-1]
    arr = []
    
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                arr.append((i,j))
    for x,y in arr:
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx <N and 0<=ny<N:
                board[nx][ny] = 1
    cnt = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 0:
                cnt +=1

    return cnt