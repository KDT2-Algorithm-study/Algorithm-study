n = int(input())

vote = []
count=0

for _ in range(n):
    vote.append(int(input()))
target = vote[0]
else_ = sorted(vote[1:], reverse=True)

if n == 1:
    print(0)
else:
    while else_[0] >= target:
        else_[0] -= 1
        target += 1
        count += 1
        else_ = sorted(else_, reverse=True)
    print(count)
