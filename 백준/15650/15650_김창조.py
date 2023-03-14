# 15650. N과 M (2)

from itertools import combinations

n, m = map(int, input().split())
lst = [num for num in range(1, n+1)]

for combination in combinations(lst, m):
    print(*combination)