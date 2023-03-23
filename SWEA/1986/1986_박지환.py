T = int(input())

for _ in range(1, T+1):
    n = int(input())
    total = 0
    for i in range(1, n+1, 2):
        total += i
    for j in range(2, n+1, 2):
        total -= j
    
    print(f'#{_} {total}')