a =int(input())
for i in range(a):
    H,W,N = map(int,input().split())
    if N%H==0:
        print(H*100+N//H)
    elif N%H<H:
        print(N%H*100 + N//H+1)