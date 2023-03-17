# 15656. N과 M (7)

import sys

n, m = map(int, sys.stdin.readline().split())
num_lst = sorted(map(int, sys.stdin.readline().split()))
comb_lst = []

def my_comb_recursion():
    if len(comb_lst) == m:
        sys.stdout.write(' '.join(map(str, comb_lst)) + '\n')
        return
    
    for num in num_lst:
        comb_lst.append(num)
        my_comb_recursion()
        comb_lst.pop()

my_comb_recursion()