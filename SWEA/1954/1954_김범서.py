direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
t = int(input())

for i in range(t):
    print(f'#{i + 1}')
    n = int(input())
    graph = [[0 for j in range(n)] for k in range(n)]
    r, c = 0, 0
    ref = 0

    for j in range(1, n ** 2 + 1):
        graph[r][c] = j
        
        r += direction[ref][0]
        c += direction[ref][1]

        if (0 <= r < n) and (0 <= c < n) and not graph[r][c]:
            continue
        else:
            r -= direction[ref][0]
            c -= direction[ref][1]
            ref = (ref + 1) % 4
            r += direction[ref][0]
            c += direction[ref][1]
    
    for j in range(n):
        print(*graph[j])

'''
# 이전 풀이

t = int(input())

for i in range(t):
    n = int(input())
    snail = [[0 for j in range(n + 2)]for k in range(n + 2)]
    x, y = 1, 1
    
    for j in range(1, n ** 2+ 1):
        if (x == 1 or snail[x - 1][y]) and (y < n or snail[x][y + 1]) and not snail[x][y + 1]:
            snail[x][y] = j
            y += 1
        elif (y == n or snail[x][y + 1]) and (x < n or snail[x + 1][y]) and not snail[x + 1][y]:
            snail[x][y] = j
            x += 1
        elif (x == n or snail[x + 1][y]) and (y > 1 or snail[x][y - 1]) and not snail[x][y - 1]:
            snail[x][y] = j
            y -= 1
        elif (y == 1 or snail[x][y - 1]) and (x > 1 or snail[x - 1][y]) and not snail[x - 1][y]:
            snail[x][y] = j
            x -= 1
        else:
            snail[x][y] = j
    
    print(f'#{i + 1}')
    for j in range(1, n + 1):
        print(*snail[j][1:n + 1])
'''
