li = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
T = int(input())

for t in range(1, T+1) :
    n = int(input())
    print(f'#{t}')
    for i in li :
        print(n // i, end=' ')
        n = n % i
    print( )