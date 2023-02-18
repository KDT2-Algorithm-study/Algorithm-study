# 1018번 체스판 다시 칠하기
# 너무 어려워서 소담님 답안을 참고해서 이해한 내용을 설명하는 풀이를 적어봤습니다

import sys
from pprint import pprint
sys.stdin = open("input.txt", "r")

H, W = map(int, input().split())
board = [ list(input()) for _ in range(H)]
B_W_paint_case = []


# 기준1 # 어떤 크기의 보드라도 왼쪽 상단 (0,0)위치를 기준으로 8*8 사이즈를 차례대로 확인한다.
# 기준2 # 어떤 보드라고 설정되는 기준값(0,0)의 위치가 'B'인 경우를 기준으로 다시 칠해야 할 위치를 카운트 한다.

for h in range(H-7):            # h는 몇번째 가로줄인지 확인
    for w in range(W-7):        # w는 몇번째 세로줄인지 확인

        # 기준점 (h,w)가 갱신될 때마다 색칠해야하는 경우를 카운트
        cnt = 0                 

        # (h,w)를 가준으로 8*8 사이즈 면적에 각 칸을 (x,y)값으로 설정한다.
        for x in range(h,h+8):  
            for y in range(w,w+8):

                # 확인 1
                # (홀x,짝y),(짝x,홀y)는 'W'이어야 한다. 
                # x+y가 홀수면 'W'이어야 한다.
                if (x+y) % 2 == 0:          
                    if board[x][y] != 'W':  

                        # 확인1,2 모두 틀리면 색칠해야 하기 때문에 카운트
                        cnt += 1            

                # 확인 2 
                # (홀x,홀y),(짝x,짝y)는 'B'이어야 한다. 
                # x+y가 짝수면 'B'이어야 한다. 
                else:                       
                    if board[x][y] != 'B':  

                        # 확인1,2 모두 틀리면 색칠해야 하기 때문에 카운트
                        cnt += 1 
                
        # cnt는 각 기준 좌표값에 기준2를 적용해서 구한 값이기 때문에 
        # 기준좌표가 'W'였을 때의 경우는 8*8 총 64칸에서 cnt를 뺀 값이 된다.
        B_W_paint_case.append(cnt)
        B_W_paint_case.append(64-cnt)

# 8*8 사이즈 보드의 경우
# 처음 기준점이 'B'혹은 'W'인 경우 
# 모두 확인한 값이 들어있는 리스트에서 가장 작은 수를 출력
print(min(B_W_paint_case))
