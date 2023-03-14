import itertools

n, r = map(int, input().split())
arr = [i for i in range(1, n+1)]
nCr = itertools.combinations(arr, r)

for x in list(nCr):
    print(*x)
    