directions = [(1, 0), (-1, 0), (0, 1), (0, -1), 
              (1, 1), (1, -1), (-1, -1), (-1, 1)]

def solution(board):
    n = len(board)
    cnt = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                stack = [(i, j)]
                while stack:
                    r, c = stack.pop()
                    if board[r][c] == 2: continue
                    board[r][c] = 2
                    cnt += 1
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if (0 <= nr < n) and (0 <= nc < n):
                            if board[nr][nc] == 0:
                                stack.append((nr, nc))
                                board[nr][nc] = 2
                                cnt += 1
    answer = n * n - cnt
    return answer
