import itertools

n, m = map(int, input().split())
for x in itertools.combinations_with_replacement(''.join([str(y) for y in range(1, n+1)]), m):
    print(*x)