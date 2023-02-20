n,m = map(int,input().split())
lst = []

def dfs():
    if len(lst) == m:
        print(*lst)
        return
    for i in range(1,n+1):
        if i not in lst:
            lst.append(i)
            dfs()
            lst.pop()
dfs()