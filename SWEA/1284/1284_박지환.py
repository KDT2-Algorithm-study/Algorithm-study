T = int(input())

for i in range(1, T+1):
    P, Q, R, S, W = map(int, input().split())
    a = P * W
    
    if W > R:
        b = Q + (W - R) * S
    else:
        b = Q
        
    print(f'#{i} {min(a, b)}')