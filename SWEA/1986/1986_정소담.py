for t in range(1,int(input())+1):
    num = 0
    for i in range(1,int(input())+1):
        if i % 2 == 1:
            num += i
        else:
            num -= i
    print(f'#{t} {num}')