T = int(input())

for _ in range(1, T+1):
    n = int(input())
    arr = list([0]*n for _ in range(n))

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    def move(x, y, cnt, r, cycle): # r은 방향을 전환하기 위한 변수, cycle은 cnt 변화없이 순환하는 횟수
        if 0 <= x + dx[r % 4] < n and  0 <= y + dy[r % 4] < n and arr[y + dy[r % 4]][x + dx[r % 4]] == 0:
            arr[y][x] += cnt
            cnt += 1
            cycle = 0
            move(x + dx[r % 4], y + dy[r % 4], cnt, r, cycle)
        
        elif cycle < 1: # 시계방향으로 돌면서 숫자를 채워나가기 때문에 cycle이 2번 이상 돌면 arr을 전부 채운 것
            r += 1
            cycle += 1
            move(x, y, cnt, r, cycle) 
            
        else:
            arr[y][x] += cnt

    move(0, 0, 1, 0, 0)
    
    print(f'#{_}')
    for i in arr:
        print(*i)