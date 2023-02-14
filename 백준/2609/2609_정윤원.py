'''
a, b = map(int, input().split())

if min(a,b) == 1 :
    print(1)
    print(max(a,b))

else :
    i = 2
    result = 1

    while i <= min(a, b) :
        if a % i == 0 and b % i == 0 :
            a = a//i
            b = b//i
            result *= i
        else : 
            i += 1
    print(result)

    i = 2
    
    while True :
        if a % i == 0 :
            a = a//i
            result *= i
        elif b % i == 0 :
            b = b//i
            result *= i
        else :
            i += 1
        
        if a == b == 1 :
            break
    print(result)
'''

# 230214 16 : 47 수정 - 'Add 2609_정윤원_code_2'

a, b = map(int, input().split())

if min(a,b) == 1 :
    print(1)
    print(max(a,b))

else :
    i = 2
    result = 1

    while i <= min(a, b) :
        if a % i == 0 and b % i == 0 :
            a = a//i
            b = b//i
            result *= i
        else : 
            i += 1
    print(result)

    result *= a*b
    print(result)