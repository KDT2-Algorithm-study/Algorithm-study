# import sys
# lst = [ int(sys.stdin.readline()) for _ in range(10) ]    
# cnt = 0
# for num in lst:
#     if cnt + num <= 100:
#         cnt += num
#     elif cnt + num > 100:
#         if 100 - cnt <= (cnt + num) - 100:
#             cnt += num
#             break
# print(cnt)

import sys
lst = [ int(sys.stdin.readline()) for _ in range(10) ]    
cnt = 0
for num in lst:
    cnt += num
    if cnt == 100:
        break
    elif cnt > 100:
        if cnt - 100 > 100 - (cnt - num):    
            cnt -= num
        break
print(cnt)
