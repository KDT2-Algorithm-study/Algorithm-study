num = int(input())
check = int(input())
l = []
if num>1:
    for i in range(num-1):
        l.append(int(input()))
    cnt = 0
    while True:
        l.sort()
        if l[-1]>=check:
            l[-1] -=1
            check +=1
            cnt +=1
        else:
            break

    print(cnt)
else:
    print(0)
