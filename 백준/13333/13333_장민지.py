n = int(input())
numbers = sorted(list(map(int, input().split())))
print(numbers)
for k in range(n,-1,-1):
  print(k)
  if k <= numbers[-k]:
    print(k)
    break