n = int(input())
i = 0
while True:
    if (n % 5) == 0:
        Box = i + (n//5)
        print(Box)
        break
    n = n-3
    i += 1
    if n < 0:
        print(-1)
        break