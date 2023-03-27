T = int(input())

for t in range(1, T+1) :
    XY = int(input())
    list1 = [[0] * XY for i in range(XY)]
    x, y = 0, -1
    dx, dy = 0, 1

    number = 1

    for i in range(XY * XY) :
        if not (0<= x + dx < XY and 0 <= y + dy < XY and list1[x + dx][y + dy] == 0) : # 범위 안에 없거나, 이미 값이 변화했으면
            if abs(dy) == 1 :
                dx, dy = dy, dx
            else : # abs(dx) == 1
                dx, dy = dy, -dx
        x += dx # 위치 이동
        y += dy # 위치 이동
        list1[x][y] = number

        number += 1
    print('#', t, sep='')
    for x in range(XY) :
        print(*list1[x])
