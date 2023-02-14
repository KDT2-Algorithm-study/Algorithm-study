# 2609 최대공약수와 최소공배수
a, b = map(int, input().split())

n = 2
result = 1
result_2 = 1
while True:
    if n > a or n > b:
        result_2 *= a
        result_2 *= b
        break
    else:
        if a % n == 0 and b % n == 0:
            result *= n
            result_2 *= n
            a = a // n
            b = b // n
        else:
            n += 1

print(result)
print(result_2)