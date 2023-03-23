T = int(input())

for t in range(T):
    N = int(input())
    arr = [[0] * N for i in range(N)]

    col, row = 0, 0
    v = 0

    arr[col][row] = 1

    dcol = [-1, 0, 1, 0]
    drow = [0, 1, 0, -1]

    for i in range(1, N**2+1):
        arr[col][row] = i
        col = col+dcol[v]
        row = row+drow[v]

        if col < 0 or row < 0 or N <= col or N <= row or arr[col][row] != 0:
            col = col-dcol[v]
            row = row-drow[v]

            v = (v+1) % 4
            col = col+dcol[v]
            row = row+drow[v]

    print(f"#{t+1}")
    for i in arr:
        for j in i:
            print(j, end=" ")
        print()