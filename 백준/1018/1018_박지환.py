import sys

n, m = map(int, sys.stdin.readline().split())
chess_board = [sys.stdin.readline().split() for _ in range(n)]
board = [[] for _ in range(n)] 
result = 0

for i in range(n):
    for j in chess_board[i][0]: # 보드 1줄을 하나하나씩 나누었음
        board[i].append(j)
        
WB_board = [[] for _ in range(8)]

for i in range(8): # 비교할 체스판 만들기
    for j in range(8):
        if (i+j) % 2 == 0:
            WB_board[j].append('W')
        else:
            WB_board[j].append('B')

for i in range(n-7):
    for j in range(m-7):
        cnt = 0
        for x in range(8):
            for y in range(8):
                if board[i+x][j+y] == WB_board[x][y]: # 보드와 체스판을 비교
                    cnt += 1 # 일치하면 1 더함
        
        cnt_max = max(cnt, 64-cnt) # BW체스판, WB체스판 중 더 비슷한 체스판으로 카운팅
        if cnt_max > result:
            result = cnt_max

print(64 - result) #  다시 칠해야 하는 정사각형 개수
                   
