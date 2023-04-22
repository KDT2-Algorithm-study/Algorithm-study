def solution(board):
    n = len(board)
    visited = [[0]*n for _ in range(n)]
    answer = 0
    stack = []
    
    dx = [1, 1, 0, -1, -1, -1, 0, 1]
    dy = [0, -1, -1, -1, 0, 1, 1, 1]
    
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                visited[i][j] = 1
                stack.append(j)
                stack.append(i)
            
            while stack:
                x = stack.pop() 
                y = stack.pop()
                
                for r in range(8):
                    if 0 <= x + dx[r] < n and 0 <= y + dy[r] < n:
                        if visited[x + dx[r]][y + dy[r]] == 0:
                            visited[x + dx[r]][y + dy[r]] = 1
        
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                 answer += 1          
   
    return answer