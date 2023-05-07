t = int(input())

for i in range(t):
    a, b = map(int, input().split())
    b %= 4
    if b == 0:
        b = 4
    result = (a ** b) % 10
    if result == 0:
        result = 10
    print(result)