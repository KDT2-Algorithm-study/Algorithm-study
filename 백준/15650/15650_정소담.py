n,m = list(map(int,input().split()))
num = []

def arr(i):
    if len(num) == m:
        print(*num)
        return
    
    for j in range(i,n+1):
        if j not in num:
            num.append(j)
            arr(j+1)
            num.pop()
arr(1)