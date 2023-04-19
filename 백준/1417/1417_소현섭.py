n = int(input())
dasom = int(input())
vote = sorted([int(input()) for _ in range(n-1)])
answer = 0
while True in list(map(lambda x:x>=dasom, vote)):
    dasom += 1
    answer += 1
    vote = sorted([vote[-1]-1]+vote[:-1])
print(answer)