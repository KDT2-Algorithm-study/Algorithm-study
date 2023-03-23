from collections import deque

for tc in range(int(input())):
    N = int(input())
    result = [[0 for _ in range(N)] for _ in range(N)] #
    deq = deque([(1,0), (0,1), (-1,0), (0,-1)]) #
    cnt = 1
    i = 0
    j = 0

    while cnt != N * N+1:
        result[j][i] = cnt
        x, y = deq[0]
        i += x
        j += y

        # 범위에 벗어나면
        if i < 0 or j < 0 or i > N-1 or j> N-1 or result[j][i] != 0:
            # 더해준 값 빼주고
            i -= x
            j -= y
            # deq값 바꿔주기
            deq.append(deq.popleft())
            x2, y2 = deq[0]
            i += x2
            j += y2

        cnt += 1
      
    print(f'#{tc+1}')
    for i in result:
        print(*i)