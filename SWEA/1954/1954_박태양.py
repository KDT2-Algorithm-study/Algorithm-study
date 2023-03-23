for tc in range(int(input())):
    n = int(input())
    lst = [[0 for _ in range(n)] for _ in range(n)]


    dir = [(1,0),(0,1),(-1,0),(0,-1)]
    k = 0 # dir
    x = 0; y = 0;    
    for i in range(1,n**2+1):
        lst[y][x] = i
        for _ in range(4):
            a,b = dir[k]
            if 0<=x+a<=n-1 and 0<=y+b<=n-1 :
                if lst[y+b][x+a] == 0:
                    x += a
                    y += b
                    break
                else:
                    k = (k+1)%4
            else:
                k = (k+1)%4

    print(f'#{tc+1}')
    for i in lst:
        print(*i)