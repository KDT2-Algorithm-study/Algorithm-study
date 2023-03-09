def pow(x, y):
    if y == 0:
        return 1
    return x * pow(x, y-1)

for _ in range(10):
    tc = int(input())
    x, y = map(int, input().split())
    print(f'#{tc} {pow(x,y)}')
