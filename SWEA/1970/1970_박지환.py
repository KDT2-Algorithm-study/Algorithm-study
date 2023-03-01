n = int(input())
money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

for i in range(1, n+1):
    m = int(input())
    res = []
    for j in range(8):
        res.append(m // money[j])
        m = m % money[j]
    
    print(f'#{i}')
    print(*res)
