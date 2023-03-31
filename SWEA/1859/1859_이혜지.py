T = int(input())

for t in range(1,T+1):
    n = int(input())
    li = list(map(int,input().split()))
    last = li[-1]
    cnt = 0
    for i in range(len(li)-1,-1,-1):
        if last > li[i]:
            cnt += last-li[i]
        else:
            last = li[i]
    print("#{} {}".format(t, cnt))