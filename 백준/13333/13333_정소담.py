n = int(input())
m = sorted(list(map(int, input().split())))
for i in range(n,-1,-1):
  if i <= m[-i]:
    print(i)
    break