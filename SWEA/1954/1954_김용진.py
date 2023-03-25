# 달팽이 숫자

import sys
sys.stdin = open('input.txt','r')


T = int(input())
di = [0, 1, 0, -1] # 이동 시킬 방향 di,dj 설정 
dj = [1, 0, -1, 0]

for t in range(1,T+1):
    N = int(input())
    arr = [[0 for _ in range(N)] for _ in range(N)] # arr을 0으로 N*N모양으로

    i,j,cnt,dr = 0, 0, 1, 0 # 초기값
    arr[i][j] = cnt # arr[0][0]의 값은 1
    cnt += 1 # 다음 자리이동하면 cnt += 1

    while cnt <= N*N: # cnt가 N*N과 같아진다면 break
        ni, nj = i+di[dr], j+dj[dr] # 기존 i,j 값에 이동 방향을 더해서 ni,nj 좌표를 바꿔줌
        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 0: # ni,nj 값이 0보다 크고 N보다 작을때 결국 최대 이동할수 있는 범위를 지정한다(못넘어가게) 그리고 해당 값이 0일때만 동작
            i, j = ni, nj # 바뀐 ni, nj 값을 i,j값으로 저장
            arr[i][j] = cnt # 바뀐 좌표에 cnt 값을 저장
            cnt += 1 # 다음 좌표를 위해 cnt += 1
        else: # 위에 조건이 아니라면 dr을 증가시켜 다음 방향으로 방향을 바꾼다.
            dr = (dr+1)%4 
    
    print(f'#{t}')
    for i in arr:
        print(*i)
