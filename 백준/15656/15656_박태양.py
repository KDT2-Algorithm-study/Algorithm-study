n, m = map(int,input().split())
l = list(map(int,input().split()))
l.sort()
lst = []
check = [False]*n
def recur(num):
    if num == m:
        return print(*lst)
    else:
        for i in range(0,n):
            if check[i] == False:
                lst.append(l[i])
                check[i] == True
                recur(num+1)
                lst.pop()
                check[i] == False

recur(0)