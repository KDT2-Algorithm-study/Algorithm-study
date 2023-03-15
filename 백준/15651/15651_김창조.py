# 15651. N과 M (3)

import sys

n, m = map(int, sys.stdin.readline().split())
lst = []

def my_comb_recursion(n: int, k: int):  
    if k == 0:
        # print(*lst)
        sys.stdout.write(' '.join(map(str, lst))+'\n')
        # ' '.join(map(str, lst))가 *lst에 비해 월등한 성능(시간차이) 기록
        # ? why
        return 
    
    for i in range(1, n+1):
        lst.append(i)
        my_comb_recursion(n, k-1)
        lst.pop()
    
my_comb_recursion(n, m)