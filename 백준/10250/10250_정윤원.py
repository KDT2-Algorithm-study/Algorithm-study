T = int(input())
for t in range(T) :
    h,w,n = map(int,input().split())
    if n % h == 0 :
            print(h * 100 + n // h)
    else :
            print((n % h) * 100 + (n // h + 1))