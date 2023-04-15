def solution(board):
    d = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
    check = []
    n = len(board)
    for i in range(n):
        for j in range(n):
            if board[j][i] == 1:
                check.append((i,j))

    for x,y in check:
        for dx,dy in d:
            mx = x+dx
            my = y+dy
            if 0<=mx<n and 0<=my<n:
                if board[my][mx] == 0:
                    board[my][mx] = -1


    answer = 0
    for i in range(n):
        for j in range(n):
            if board[j][i] == 0:
                answer +=1
    
    return answer

b = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]
print(solution(b))