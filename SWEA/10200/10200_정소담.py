for t in range(int(input())):
    n,a,b = map(int,input().split())
    print(f'#{t+1} {min(a,b)} {max(0,a+b-n)}')