for t in range(1,int(input())+1):
    p,q,r,s,w = map(int,input().split())
    if w > r:
        print(f'#{t}',min(w * p, q + (w - r) * s))
    else:
        print(f'#{t}',min(w * p, q))