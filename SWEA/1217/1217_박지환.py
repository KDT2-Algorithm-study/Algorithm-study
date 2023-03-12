for i in range(10):
    k = int(input())
    n, m = map(int, input().split())
    num, cnt = 1, 0
        
    def recur(num, cnt):
        if cnt == m:
            return num
        else:
            num *= n
            cnt += 1
            recur(num, cnt)
            
    print(f'#{k} {recur(num, cnt)}')