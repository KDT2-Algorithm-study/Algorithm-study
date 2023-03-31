# 11399. ATM

n = int(input())
num_lst = map(int, input().split())

answer = 0
tmp = 0
for num in sorted(num_lst):
    tmp += num
    answer += tmp
    
print(answer)