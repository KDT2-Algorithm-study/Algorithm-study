n = int(input())

def fibonacci(n):
    fn_1, fn_2 = 1, 0
    
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        for i in range(n-1):
            fn = fn_1 + fn_2
            fn_2 = fn_1
            fn_1 = fn
        
        return fn

print(fibonacci(n))