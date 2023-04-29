n = int(input())
stair = [int(input()) for _ in range(n)]
stack = [0] * n

if n < 3:
  print(sum(stair))
elif n == 3:
  print(max(stair[0], stair[1]) + stair[2])
elif n > 3:
  stack[0] = stair[0]
  stack[1] = stair[0]+stair[1]
  stack[2] = max(stair[0], stair[1]) + stair[2]
  for i in range(3,n):
      stack[i] = max(stair[i-1]+stack[i-3], stack[i-2]) + stair[i]
  print(stack[-1])