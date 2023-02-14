# 최대공약수와 최소공배수

a,b = map(int,input().split())

num_max = []

for i in range(1, 10000): 
    if a % i == 0 and b % i ==0: 
        num_max.append(i)
print(max(num_max))
print(max(num_max) * ((a//max(num_max))* (b//max(num_max))))
