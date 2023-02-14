# 2609. 최대공약수와 최소공배수

import sys
import math

# input
a_num, b_num = map(int, sys.stdin.readline().strip().split())

''' 
# solution1 - factorization
# solution2에 비해 메모리 미세하게 더 쓰고 시간 미세하게 더 빠름
def get_primary_lst(n: int):
    # Use Eratosthenes Sieve
    lst = [i for i in range(n + 1)]
    lst[0], lst[1] = False, False
    
    for i in range(2, int(math.sqrt(n)) + 1):
        if lst[i]:
            j = i * 2
            while j <= n:
                lst[j] = False
                j += i
                
    return lst

def get_factorization(n: int, lst: list):
    dict_ = {}
    
    while n > 1:
        for primary in lst:
            # primary가 소수가 아닌 경우
            if not primary:
                continue
            
            # primary가 소수인 경우
            if n % primary == 0:
                dict_[primary] = dict_.get(primary, 0) + 1
                n //= primary
                break
        
    return dict_

def get_maximum_common_div(a: dict, b: dict):
    num_sum = 1
    
    # 두 수 중 하나가 1이면
    if not a or not b:
        return 1
    
    for k, v in a.items():
        if k in b:
            num_sum *= pow(k, v) if v < b[k] else pow(k, b[k])
            
    return num_sum
                

def get_minimum_common_mult(a: dict, b: dict):
    num_sum = 1
    
    # 두 수 중 하나가 1이면
    if not a or not b:
        return max(a_num, b_num)
    
    for k, v in a.items():
        if k in b:
            num_sum *= pow(k, v) if v > b[k] else pow(k, b[k])
        else:
            num_sum *= pow(k, v)
            
    for k, v in b.items():
        if k not in a:
            num_sum *= pow(k, v)
            
    return num_sum


primary_lst = get_primary_lst(a_num) if a_num > b_num else get_primary_lst(b_num)
a_dict, b_dict = get_factorization(a_num, primary_lst), get_factorization(b_num, primary_lst)
# print
# Print maximum common div
print(get_maximum_common_div(a_dict, b_dict))
# Print minimum common mult
print(get_minimum_common_mult(a_dict, b_dict))
'''

# solution2
mcd = 0
for i in range(a_num if a_num < b_num else b_num, 0, -1):
    if a_num % i == 0 and b_num % i == 0:
        mcd = i
        break
    
print(mcd)
print(a_num * b_num // mcd)