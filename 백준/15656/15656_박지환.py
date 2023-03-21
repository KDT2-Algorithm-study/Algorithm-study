from itertools import product

n, m = map(int, input().split())
num_list = list(map(int, input().split()))
num_list = sorted(num_list)

pd = product(num_list, repeat = m)

for i in pd:
    print(*i)