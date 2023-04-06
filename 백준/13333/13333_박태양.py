n = int(input())
lst = sorted(list(map(int, input().split())))
for k in range(n,-1,-1):
  if k <= lst[-k]:
    print(k)
    break