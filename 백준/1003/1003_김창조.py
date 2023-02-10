# 1003. 피보나치 함수

import sys
import math
import time
import datetime

''' memory out of range
from functools import cache

# solution
@cache
def fibonacci_count(num: int, zero: int, one: int):
    if num == 0:
        zero += 1
        return 0, zero, one
    elif num == 1:
        one += 1
            return 1, zero, one
    num1, zero, one = fibonacci_count(num - 1, zero, one) 
    num2, zero, one = fibonacci_count(num - 2, zero, one)
    return num1 + num2, zero, one



# input & print
n_num = int(sys.stdin.readline().strip())   # None strip int(str)는 많은 시간을 소모
for _ in range(n_num):
    zero_cnt, one_cnt = 0, 0
    input_num = int(sys.stdin.readline().strip())
    start = time.time()
    result, zero_cnt, one_cnt = fibonacci_count(input_num, zero_cnt, one_cnt)
    print(zero_cnt, one_cnt)
    
    # Time measure
    end = time.time()
    print(datetime.timedelta(seconds = end - start))
'''

# input & print
n_num = int(sys.stdin.readline().strip())
for _ in range(n_num):
    zero_cnt, one_cnt = 0, 0
    input_num = int(sys.stdin.readline().strip())
    
    # Time measure start
    # start = time.time()
    
    idx = 0
    cnt_lst = []
    # only count '0' and '1'
    for idx in range(input_num + 1):
        if idx == 0:
            cnt_lst.append([1, 0])
        elif idx == 1:
            cnt_lst.append([0, 1])
        else:
            cnt_lst.append([cnt_lst[idx-1][0] + cnt_lst[idx-2][0], cnt_lst[idx-1][1] + cnt_lst[idx-2][1]])
        
    print(*cnt_lst.pop())
    
    # Time measure
    # end = time.time()
    # print(datetime.timedelta(seconds = end - start))