# 1018.
Y, X = map(int, input().split())
matrix = [input() for y in range(Y)]
# print(matrix)

min_cnt = 64

for y1 in range(Y-8+1) :
    for x1 in range(X-8+1) :

        # if matrix[y1][x1] == 'W' :
        # col1 = 'W'
        # col2 = 'B'
        # else :
        col1 = 'B'
        col2 = 'W'

        cnt = 0

        for y2 in range(8) :
            for x2 in range(8) :
                # print(matrix[y2+y1][x2+x1], end='')
                if (x2 + y2) % 2 == 0 and matrix[y2+y1][x2+x1] != col1:
                    cnt += 1
                elif (x2 + y2) % 2 == 1 and matrix[y2+y1][x2+x1] != col2:
                    cnt += 1
            # print()
        # print()
        min_cnt = min(min_cnt, cnt, 64-cnt)

print(min_cnt)
