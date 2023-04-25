n = int(input())
dasom = int(input()) 
vote = [] 
cnt = 0 
for _ in range(n - 1):
  vote.append(int(input()))

vote.sort(reverse=True)

if n == 1:
  print(0)
else:
  while vote[0] >= dasom:
    dasom += 1
    vote[0] -= 1
    cnt += 1
    vote.sort(reverse=True)
  print(cnt)