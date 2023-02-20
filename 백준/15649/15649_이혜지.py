n, m = map(int, input().split())
li = []

def dfs(a) :
    if a == m :
        print(*li)
        return
    else :
        for i in range(1, n+1) :
            if i not in li :
                li.append(i)
                dfs(a + 1)
                li.pop()

dfs(0)