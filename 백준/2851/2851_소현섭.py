mush = [int(input()) for _ in range(10)]
answer = 0
for x in range(1, 10):
    mush[x] += mush[x-1]
for y in mush:
    if abs(100-answer) >= abs(100-y):
        answer = y
print(answer)