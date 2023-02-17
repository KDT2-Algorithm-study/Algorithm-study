# 체스판 다시 칠하기
# 답지를 보고.. 혼자서 해석만 했습니다...
n, m = map(int, input().split())
board = []
result = []
 
for _ in range(n):
    board.append(input()) # WB들을 리스트에 넣어준다.
 
for i in range(n-7): # 판의 크기 만큼 빼서 8x8 일때 전부다 돌수있게
    for j in range(m-7):
        draw1 = 0
        draw2 = 0
 
        for a in range(i, i+8):  # 8 칸씩 모든 리스트 조회
            for b in range(j, j+8): 
                if (a + b) % 2 == 0: # 홀수일떄
                    if board[a][b] != 'B':  # board[i]번째 리스트의 홀수번째 리스트
                        draw1 += 1 # 1번 카운트
                    if board[a][b] != 'W':  # board[i]번째 리스트의 짝수번째 리스트 
                        draw2 += 1
                else:# 짝수일떄
                    if board[a][b] != 'W': # board[i]번째 리스트의 홀수번째 리스트
                        draw1 += 1
                    if board[a][b] != 'B':# board[i]번째 리스트의 짝수번째 리스트
                        draw2 += 1
 
        result.append(draw1)
        result.append(draw2)
 
print(min(result))