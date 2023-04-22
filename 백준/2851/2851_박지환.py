mushroom = [int(input()) for _ in range(10)]
total = 0
min_diff = 100
res = []

for i in mushroom:
    total += i
    
    if abs(total - 100) < min_diff:
        min_diff = abs(total - 100)
        res.clear()
        res.append(total)
        
    elif abs(total - 100) == min_diff:
        res.append(total)

print(res[-1])