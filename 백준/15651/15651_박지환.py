# 나머지로 계산

# n, m = map(int, input().split())
# num_list =[_ for _ in range(1, n+1)]
# arr = [n**k for k in range(m-1, -1, -1)]

# for i in range(n**m):
#     for j in range(m):
#         print(((i // arr[j]) % n) + 1, end = ' ')
#     print('')

#=================================================
# 중복 순열

from itertools import product

n, m = map(int, input().split())
num = [i for i in range(1, n+1)]

answer = list(product(num, repeat = m))

for x in answer:
    print(*x)
    
#==================================================
# dfs - 이해 못함

# n, m = map(int,input().split())
 
# arr = []
 
# def dfs():
#     if len(arr) == m:
#         print(' '.join(map(str, arr)))
#         return
    
#     for i in range(1, n+1):
#         arr.append(i)
#         dfs()
#         arr.pop()
# dfs()
