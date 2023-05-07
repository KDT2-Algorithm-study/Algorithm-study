score = {(1, 3): 'A', (2, 2): 'B', (3, 1): 'C', (4, 0): 'D', (0, 4): 'E'}

for i in range(3):
    temp = list(map(int, input().split()))
    zero = 0
    one = 0
    for num in temp:
        if num == 0:
            zero += 1
        else:
            one += 1
    print(score[(zero, one)])