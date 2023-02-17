n, m = map(int, input().split())
chess = [list(input()) for _ in range(n)]
answer = 64
for x in range(n-8+1):
    for y in range(m-8+1):
        w_index, b_index = 0, 0
        for i in range(x, x+8):
            for j in range(y, y+8):
                if (i+j) % 2 == 1:
                    if chess[i][j] == 'W':
                        w_index += 1
                    else:
                        b_index += 1
                else:
                    if chess[i][j] == 'B':
                        w_index += 1
                    else:
                        b_index += 1
        if answer >= min(w_index, b_index):
            answer = min(w_index, b_index)
print(answer)