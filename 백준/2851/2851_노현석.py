mushroom = [int(input()) for _ in range(10)]
score = 0

for idx in range(9):
    score += mushroom[idx]
    temp = score + mushroom[idx+1]

    if temp >= 100:
        if (100 - score) >= (temp - 100):
            score = temp
        break
else:
    score += mushroom[-1]
print(score)