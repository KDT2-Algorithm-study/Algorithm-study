n,m = map(int,input().split())
num = list(map(int,input().split()))
num.sort()
lst = []

def arr():
    if len(lst) == m:
        print(*lst)
        return
    
    for i in num:
            lst.append(i)
            arr()
            lst.pop()
arr()