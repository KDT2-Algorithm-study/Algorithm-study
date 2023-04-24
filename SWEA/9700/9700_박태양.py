tc = int(input())
for i in range(tc):
    p,q = map(float,input().split())
    
    t1 = (1-p)*q
    t2 = p*(1-q)*q

    if t1<t2:
        print(f'#{i+1} YES')
    else:
        print(f'#{i+1} NO')