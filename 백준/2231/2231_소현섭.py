n = int(input())
for num in range(n):
    answer, m = num, 0
    while num > 0:
        m += num % 10
        num //= 10
    if n == answer+m:
        print(answer)
        break
else:
    print(0)