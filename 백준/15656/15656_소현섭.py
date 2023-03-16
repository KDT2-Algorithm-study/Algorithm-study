import sys
import itertools

n, m = map(int, sys.stdin.readline().split())
for x in itertools.product(sorted(list(map(int, sys.stdin.readline().split()))), repeat=m):
    print(*x)