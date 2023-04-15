n = int(input())
lst = sorted(list(map(int, input().split())))
for i in range(n, -1, -1):
    if i <= lst[-i]:
      print(i)
      break      
