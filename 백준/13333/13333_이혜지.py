n = int(input())
li = sorted(list(map(int, input().split())))

for k in range(n,-1,-1):
  if k <= li[-k]:
    print(k)
    break