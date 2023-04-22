n = int(input())

for i in range(1, n+1):
    p, q = map(float, input().split())
    
    if (1 - p) * q < p * (1 - q) * q:
        print(f'#{i} YES')
    else:
        print(f'#{i} NO')
    
        
    