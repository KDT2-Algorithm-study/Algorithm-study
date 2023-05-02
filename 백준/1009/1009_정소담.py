for i in range(int(input())):
    a,b = map(int,input().split())
    c=(a**(b%4+4))%10
    if c == 0:
        print(10)
    else:
        print(c)