for i in range(int(input())):
    lst = [0]*5
    t = int(input())
    while t>1:
        if t%2 == 0:
            t //=2
            lst[0] +=1
        if t%3 == 0:
            t //=3
            lst[1] +=1
        if t%5 == 0:
            t //=5
            lst[2] +=1
        if t%7 == 0:
            t //=7
            lst[3] +=1
        if t%11 == 0:
            t //=11
            lst[4] +=1
    
    print(f'#{i+1}',end=' ')
    print(*lst)