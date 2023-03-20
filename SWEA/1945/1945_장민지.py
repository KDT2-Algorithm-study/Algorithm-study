prime_nums = [2, 3, 5, 7, 11]

T = int(input())
for t in range(1, T+1):
    N = int(input())
    index = 0
    divisor = [0] * 5
    
    for num in prime_nums:
        prime_cnt = 0

        while N % num == 0:
            prime_cnt += 1
            N = N / num

        divisor[index] = prime_cnt
        index += 1
    
    print(f"#{t}", *divisor)