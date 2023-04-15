tc = int(input())
for i in range(tc):
    m,a,b = map(int,input().split())
    print(f'#{i+1} {min(a,b)} {max(a+b-m,0)}')
