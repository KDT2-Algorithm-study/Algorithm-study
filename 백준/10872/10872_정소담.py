
# while 문
# 코드길이 66B/ 시간 40ms/ 메모리 31256 KB
n = int(input())
m = 1
while n > 0:
    m *= n
    n -= 1
print(m)

# for 문
# 코드길이 59B/ 시간 36ms/ 메모리 30616 KB
m = 1
for i in range(1,int(input())+1):
    m *= i
print(m)