n,m = list(map(int,input().split()))
num = []

def arr(i):
    if len(num) == m:
        print(*num)
        return
    
    for j in range(1,n+1):
            num.append(j)
            arr(j)
            num.pop()
arr(1)