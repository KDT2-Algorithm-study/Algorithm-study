T = int(input())

for t in range(1, T+1) :
    n, a, b = map(int, input().split())

    if n > (a+b) :
        minn = 0
    else :
        minn = a+b-n

    print(f'#{t} {min(a, b)} {minn}')        