for t in range(1,int(input())+1):
    n = int(input())
    price = list(map(int,input().split()))
    sell = 0
    cnt = 0
    for i in reversed(price):
        if sell < i:
            sell = i
        else:
            cnt += (sell-i)
    print(f'#{t} {cnt}')