import sys

n = input()
time_list = list(map(int, sys.stdin.readline().split()))

time_list = sorted(time_list, reverse=True)
total = 0
for i in range(len(time_list)):
    total += (i + 1) * time_list[i]

print(total)