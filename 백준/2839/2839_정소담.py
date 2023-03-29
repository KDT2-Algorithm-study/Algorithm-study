n = int(input())

a = n % 5
b = n // 5
x = [1, 2, 4, 7]

if n in x:
    print(-1)
else:
    if a == 0:
        print(b)
    elif a % 2 == 1:
        print( b + 1 )
    elif a % 2 == 0:
        print( b + 2 )