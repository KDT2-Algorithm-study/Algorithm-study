# 1715. 카드 정렬하기

import heapq
import sys

n = int(sys.stdin.readline())
nums = []

for _ in range(n):
    nums.append(int(sys.stdin.readline()))

heapq.heapify(nums)

answer = 0
while len(nums) > 1:
    tmp = heapq.heappop(nums) + heapq.heappop(nums)
    answer += tmp
    heapq.heappush(nums, tmp)
    
print(answer)