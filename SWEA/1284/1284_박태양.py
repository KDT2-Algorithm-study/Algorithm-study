for i in range(int(input())):
    p,q,r,s,w = map(int,input().split())
    a = p*w
    if w<=r:
        b = q
    else:
        b = q+(w-r)*s
    
    print(f'#{i+1} {min(a,b)}')