
for tc in range(int(input())):
    num = int(input())
    lst = list(map(int,input().split()))
    e = 0
    total = 0
    for i in range(num-1,-1,-1):
        if lst[i]>e:
            e = lst[i]
        else:
            total += e-lst[i]

    print(f'#{tc+1} {total}')
