for _ in range(int(input())):
    x,y = 1,0
    n = int(input())
    if n == 0:
        print(x, y)
    else:
        for _ in range(n):
            x,y = y,x+y
        print(x,y)