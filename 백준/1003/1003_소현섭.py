for _ in range(int(input())):
    zero_count, one_count = 1, 0
    for x in range(int(input())):
        zero_count, one_count = one_count, zero_count+one_count
    print(zero_count, one_count)