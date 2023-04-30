# 7576. 토마토

import sys
import copy
from collections import deque
from pprint import pprint
input = sys.stdin.readline

M, N = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]

answer = [0]
DELTA = [(0, 1), (0, -1), (1, 0), (-1, 0)]

q = deque()
for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            q.append((i, j))
            
cnt = 0
while q:
    tmp = 0
    tmp_q = []
    
    # 하루 동안 새로 익은 토마토의 주변을 동시에 검사
    # 해당 날짜에 익은 토마토들의 값 변화와 cnt 값 증가를 동시에 진행
    for y, x in q:
        tmp += 1    # q에서 제거할 갯수
        for dy, dx in DELTA:
            ny, nx = y+dy, x+dx
            if 0 <= ny < N and 0 <= nx < M:
                if not box[ny][nx]:
                    # 추가 값(새로 익을 토마토)
                    tmp_q.append((ny, nx))
                    box[ny][nx] = 2
    q += tmp_q
    # 연산 종료 후 q에서 사용된 값(이미 익은 토마토) 제거
    for _ in range(tmp):
        q.popleft()
            
    cnt += 1

cnt -= 1    # 모든 토마토가 익고 난 후 검사한 cnt 1 감소
answer.append(cnt)

check_zero = [line.count(0) for line in box]
for cnt in check_zero:
    if cnt:
        print(-1)
        break
else:
    print(max(answer))