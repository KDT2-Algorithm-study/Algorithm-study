li = []
score = 0

for _ in range(10):
    li.append(int(input()))

for i in li:
    score += i
    if score >= 100:
        if score - 100 > 100 - (score - i):
            score -= i
        break

print(score)