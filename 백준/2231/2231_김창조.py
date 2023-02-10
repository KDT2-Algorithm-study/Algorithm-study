# 2231. 분해합_김창조

import sys


# input
n_num = int(sys.stdin.readline())

# solution
n_digit_num = len(str(n_num))
construct_num = 10**(n_digit_num - 1) - 9*n_digit_num
construct_num = 0 if construct_num < 0 else construct_num
while construct_num < n_num:
    # Make construction
    sum_num = construct_num
    for single_digit in str(construct_num):
        sum_num += "0123456789".index(single_digit)
    
    # Find min constructor
    if sum_num == n_num:
        break
    
    construct_num += 1
else:
    construct_num = 0
    
# print
print(construct_num)