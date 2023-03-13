def factorial_recursion(n: int):
    if n == 0 or n == 1:
        return 1
    
    return factorial_recursion(n-1) * n


print(factorial_recursion(int(input())))