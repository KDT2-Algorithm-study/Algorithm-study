T = int(input())

for _ in range(1, T+1):
    n = int(input())
    num_dict = {2: 0, 3: 0, 5: 0, 7: 0, 11: 0}
    while True:
        if n % 2 == 0:
            n = n // 2
            num_dict[2] += 1
            
        elif n % 3 == 0:
            n = n // 3
            num_dict[3] += 1
            
        elif n % 5 == 0:
            n = n // 5
            num_dict[5] += 1
            
        elif n % 7 == 0:
            n = n // 7
            num_dict[7] += 1
            
        elif n % 11 == 0:
            n = n // 11
            num_dict[11] += 1
            
        else:
            break
    print(f'#{_}', end = ' ')
    print(*num_dict.values())