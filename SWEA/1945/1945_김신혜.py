# import sys
# sys.stdin = open("input.txt", "r")
T = int(input())
numbers = [2, 3, 5, 7, 11]
for t in range(1, T+1):
    lst = [0, 0, 0, 0, 0]
    N = int(input())
    for i in range(5):
        while N >= numbers[i]:
            if N % numbers[i] == 0:
                N /= numbers[i]
                lst[i] += 1
            else:
                break
    print(f'#{t}',*lst)
