n, k = map(int, input().split())
num_list = [i for i in range(1, n+1)]

result = []
start = k-1

while len(num_list) != 1: # 마지막 값만 남으면 break
    result.append(num_list.pop(start))
    start += k-1
    while start > (len(num_list)-1):
        start = start - len(num_list)
result.append(num_list.pop()) # 마지막 값 담아주기

print("<", end="")
print(*result,sep=", ",end="")
print(">")
