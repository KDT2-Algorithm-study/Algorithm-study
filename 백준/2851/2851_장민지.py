result = 0
for _ in range(10):
    n = int(input())
    result += n
    if result >= 100:
        if result - 100 > 100 - (result - n):
            result -= n
        break
print(result)