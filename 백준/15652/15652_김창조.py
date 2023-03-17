# 15652. N과 M (4) 

n, m = map(int, input().split())
lst = []

def my_comb_recursion(k: int):
    if len(lst) == m:
        print(' '.join(map(str, lst)))    
        return
    
    for i in range(k, n+1):
        lst.append(i)
        my_comb_recursion(i)
        lst.pop()
    
my_comb_recursion(1)