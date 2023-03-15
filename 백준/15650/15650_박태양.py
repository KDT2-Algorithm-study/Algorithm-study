n, m = map(int,input().split())
l = []
check = [False]*(n+1)
def recur(num):
    if num == m:
        return print(*l)
    else:
        for i in range(1,n+1):
            if check[i] == False:
                for j in range(1, i+1):
                    check[j] = True
                l.append(i)
                recur(num+1)
                for j in range(1, i+1):
                    check[j] = False
                l.pop()

recur(0)