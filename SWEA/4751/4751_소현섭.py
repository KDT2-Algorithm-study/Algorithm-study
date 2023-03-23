T = int(input())
for test_case in range(1, T + 1):
    s = input()
    w = 1+4*(len(s))
    li = [['.']*w for _ in range(5)]
    i = 0
    for x in range(2, w, 4):
        li[0][x] = '#'
        li[4][x] = '#'
        li[2][x] = s[i]
        i += 1
    for y in range(1, w, 2):
        li[1][y] = '#'
        li[3][y] = '#'
    for z in range(0, w, 4):
        li[2][z] = '#'
    for l in li:
        print(''.join(l))