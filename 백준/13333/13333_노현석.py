n = int(input())
nums = list(map(int, input().split()))
nums = sorted(nums)

for i in range(n, -1, -1):
    if i <= nums[-i]:
        print(i)
        break
