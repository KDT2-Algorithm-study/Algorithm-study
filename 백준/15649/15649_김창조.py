# 15649. N과 M (1)

import sys
from itertools import combinations

n, c = map(int, sys.stdin.readline().rstrip().split())

comb_lst = list(combinations([num for num in range(1, n+1)], c))

for lst in comb_lst:
    print(*lst)