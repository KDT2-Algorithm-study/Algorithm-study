# 2851. 슈퍼 마리오

import sys

answer = 0
for _ in range(10):
    num = int(sys.stdin.readline())
    if answer < 100:
        answer_small = answer
        answer += num
    
if answer - 100 > 100 - answer_small:
    answer = answer_small
    
print(answer)