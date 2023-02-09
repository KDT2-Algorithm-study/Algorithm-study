# import sys
# sys.stdin = open('test.txt', 'r')

T = int(input())

for t in range(T) : 

    ''' 
    # 1. 시간 초과
    number = int(input())
    list_num = [number]
    # print(list_num)
    cnt_1 = 0
    cnt_0 = 0

    while (list_num) :
        temp = list_num.pop()
        if temp >= 2 :   
            list_num.append(temp-1)
            list_num.append(temp-2)
        elif temp == 1 :
            cnt_1 += 1
        elif temp == 0 :
            cnt_0 += 1

    print(cnt_0, cnt_1)
    '''

    # 직접 출력해서 규칙 발견

    ''' 
    # 2. 
    number = int(input())
    a, b = 1, 0

    for i in range(number) :
        temp_a, temp_b = a, b
        a, b = temp_b, temp_a + temp_b

    print(a,b)
    '''

    # 3. 
    number = int(input())
    a, b = 1, 0

    for i in range(number) :
        a, b = b, a + b

    print(a,b)
