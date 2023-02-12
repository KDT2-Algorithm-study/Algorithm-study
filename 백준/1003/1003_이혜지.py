T = int(input())

for t in range(1, T+1) :
    n = int(input())
    if n == 0 :
        print(1, 0)
    # elif n == 1 :
    #     print(0, 1)
    else :
        a = 0
        b = 1
        sum_0 = 0
        sum_1 = 1

        for _ in range(n-1) :   
            sum_0 = sum_1
            sum_1 = a + b
            # print(a, b, sum_0, sum_1)
            a = b
            b = sum_1
            
            
        print(sum_0, sum_1)        

