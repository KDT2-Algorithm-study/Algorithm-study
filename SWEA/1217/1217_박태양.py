def sqrt(a,b):
    if b == 0:
        return 1
    else:
        return a*sqrt(a,b-1)

for i in range(10):
    a = int(input())
    x,y = map(int,input().split())
    print(f'#{i+1} {sqrt(x,y)}')


