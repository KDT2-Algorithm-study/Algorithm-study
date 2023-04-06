n = int(input())
li = sorted(list(map(int, input().split())))
answer = 0
for i in range(li[-1], -1, -1):
    if len(list(filter(lambda x: x >= i, li))) >= i:
        answer = i
        break
print(answer)