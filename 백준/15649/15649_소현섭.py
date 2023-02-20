import itertools

n, m = map(int, input().split())
for x in itertools.permutations(''.join([str(y) for y in range(1, n+1)]), m):
    print(*x)