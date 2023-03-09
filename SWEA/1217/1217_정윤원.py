def nloop(n, m) :
    if m > 0 :
        return n * nloop(n, m-1)
    else :
        return 1

for t in range(10) :
    input()
    n, m = map(int, input().split())
    print(f"#{t+1} {nloop(n, m)}")