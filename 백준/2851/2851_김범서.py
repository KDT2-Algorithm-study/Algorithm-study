mushroom = list()
total = list()
result = 0

for i in range(10):
    score = int(input())
    mushroom.append(score)
    if not i:
        total.append(score)
    else:
        total.append(total[i - 1] + score)

for i in range(10):
    if total[i] <= 100:
        result = total[i]
    else:
        if (total[i] - 100) <= (100 - result):
            result = total[i]
        break

print(result)
